from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PredictionForm
from .model_utils import make_prediction
import os
import csv
import joblib
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # for headless server rendering
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'predictor/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'predictor/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('predict')
        else:
            return render(request, 'predictor/login.html', {'error': 'Invalid credentials'})
    return render(request, 'predictor/login.html')

@login_required
def predict(request):
    prediction = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = make_prediction(data)
            prediction = 'Employee will LEAVE' if result == 1 else 'Employee will STAY'
    else:
        form = PredictionForm()
    return render(request, 'predictor/predict.html', {'form': form, 'prediction': prediction})

def calculate_model_accuracy():
    """
    Calculate the accuracy of the model.
    :return: Accuracy as a float.
    """
    model_path = os.path.join('predictor', 'final_model.pkl')
    model = joblib.load(model_path)

    test_data_path = os.path.join('predictor', 'Cleaned_Employee.csv')
    test_data = pd.read_csv(test_data_path)

    X_test = test_data.drop('LeaveOrNot', axis=1)
    y_test = test_data['LeaveOrNot']

    predictions = model.predict(X_test)
    accuracy = (predictions == y_test).mean()

    # Confusion matrix
    from sklearn.metrics import confusion_matrix
    conf_matrix = confusion_matrix(y_test, predictions)

    return accuracy, conf_matrix
    

@login_required
def dashboard(request):
    csv_file_path = os.path.join('predictor', 'Cleaned_Employee.csv')
    absolute_csv_path = os.path.abspath(csv_file_path)

    total_records, num_features, leave_count, stay_count = process_csv_file(absolute_csv_path)

    if total_records is None:
        return render(request, 'predictor/dashboard.html', {'error': 'CSV file error.'})

    accuracy, conf_matrix = calculate_model_accuracy()

    # Generate charts
    pie_chart_path = os.path.join('predictor', 'static', 'predictor', 'pie_chart.png')
    bar_chart_path = os.path.join('predictor', 'static', 'predictor', 'bar_chart.png')
    generate_pie_chart(leave_count, stay_count, pie_chart_path)
    generate_bar_chart(leave_count, stay_count, bar_chart_path)

    stats = {
        'total_records': total_records,
        'num_features': num_features,
        'leave_count': leave_count,
        'stay_count': stay_count,
        'accuracy': accuracy,
        'conf_matrix': conf_matrix.tolist(),  # convert numpy array to list for JSON-safe
        'pie_chart_url': '/static/predictor/pie_chart.png',
        'bar_chart_url': '/static/predictor/bar_chart.png',
    }

    return render(request, 'predictor/dashboard.html', {'stats': stats})

def process_csv_file(file_path):
    """
    Process the CSV file and calculate total records, leave count, and stay count.
    :param file_path: Path to the CSV file.
    :return: Tuple (total_records, leave_count, stay_count) or (None, None, None) if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        total_records = len(df)
        num_features = len(df.columns) - 1  # excluding target column
        leave_count = df['LeaveOrNot'].value_counts().get(1, 0)
        stay_count = df['LeaveOrNot'].value_counts().get(0, 0)

        return total_records, num_features, leave_count, stay_count
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return None, None, None, None

def generate_pie_chart(leave_count, stay_count, save_path):
    labels = ['Leave', 'Stay']
    sizes = [leave_count, stay_count]
    colors = ['red', 'green']
    plt.figure(figsize=(4,4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.axis('equal')
    plt.savefig(save_path)
    plt.close()

def generate_bar_chart(leave_count, stay_count, save_path):
    categories = ['Leave', 'Stay']
    counts = [leave_count, stay_count]
    colors = ['red', 'green']
    plt.figure(figsize=(5,4))
    plt.bar(categories, counts, color=colors)
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.title('Leave vs Stay Count')
    plt.savefig(save_path)
    plt.close()

def user_logout(request):
    logout(request)
    return redirect('home')
