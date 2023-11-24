from  .models import *


import random


student_names = [
    "Manideep","Abhinay Reddy", "Sonam", "Priya", "Rahul", "Ananya", "Akshay", "Sneha", 
    "Vikas", "Pooja", "Arjun", "Neha", "Ravi", "Anjali", "Rohit", "Aishwarya", 
    "Karthik", "Shreya", "Deepak", "Simran", "Varun", "Kavya", "Aditya", "Tanvi", 
    "Prakash", "Shilpa", "Siddharth", "Kritika", "Gaurav", "Shruti", "Raj", "Anushka", 
    "Naveen", "Preeti", "Praveen", "Aanya", "Raghav", "Sushma", "Vinay", "Ishita", 
    "Arnav", "Vaishnavi", "Kishore", "Sakshi", "Akash", "Anika", "Parth", "Riya", 
    "Yash", "Aarohi", "Ankit", "Aarushi", "Manish", "Snehal", "Niharika", "Rohan", 
    "Shubham", "Muskan", "Ashwin", "Tanisha", "Shiva", "Poonam", "Harish", "Keerthi", 
    "Kunal", "Anjana", "Aditi", "Deepika", "Mayank", "Prisha", "Jatin", "Suman", 
    "Shashank", "Khushi", "Anand", "Vishal", "Muskaan", "Rajat", "Bhavna", "Anurag", 
    "Nandini", "Utkarsh", "Saumya", "Vibhav", "Aaradhya", "Sameer", "Ishika", "Soham", 
    "Kavya", "Suraj", "Arpita", "Abhay", "Kanika", "Tanay", "Anvi", "Shubhang", 
    "Bhavya", "Anirudh", "Priyanka", "Siddhi", "Pranav", "Tanya", "Rishi", "Ishika", 
    "Sumit", "Ananya", "Adarsh", "Snehal", "Aishwarya", "Rohit", "Swara", "Akshat", 
    "Khushbu", "Satish", "Divya", "Deepak", "Varsha", "Yuvraj", "Nisha", "Amol", 
    "Neha", "Omkar", "Kirti", "Rohit", "Shalini", "Sagar", "Ankita", "Avinash", 
    "Riya", "Ritesh", "Shweta", "Akshara", "Siddharth", "Ashwini", "Rohan", "Anusha", 
    "Pratik", "Anjali", "Gaurav", "Sheetal", "Aditya", "Suman", "Varun", "Shruti", 
    "Mayank", "Pooja", "Shivam", "Rashmi", "Akhil", "Anushka"
]


Parents = [
    "Surakshana Reddy", "Surakshana Reddy", " Suresh", "Ananya Venkatesh", "Anand Raju", 
    "Anika Sharma", "Anirudh Naidu", "Anjali Reddy", "Anurag Kumar", "Aarohi Patel", 
    "Bhavna Singh", "Chaitanya Kumar", "Deepika Reddy", "Gaurav Raj", "Haritha Reddy", 
    "Ishita Sharma", "Karthik Reddy", "Kavya Naidu", "Kiran Kumar", "Kirti Sharma", 
    "Krishna Raju", "Lakshmi Naidu", "Manoj Kumar", "Meera Reddy", "Nandini Singh", 
    "Naveen Kumar", "Niharika Naidu", "Nikhil Reddy", "Pooja Sharma", "Prakash Raj", 
    "Priya Reddy", "Rahul Kumar", "Rajesh Naidu", "Rani Singh", "Ravi Kumar", 
    "Rishi Sharma", "Rohit Reddy", "Sakshi Naidu", "Sameer Kumar", "Shilpa Raj", 
    "Shiva Naidu", "Shruti Sharma", "Sneha Reddy", "Suman Naidu", "Suresh Kumar", 
    "Tanvi Sharma", "Varun Reddy", "Vikas Kumar", "Vinay Naidu", "Yash Raj",
    "Aaditi Venkatesh", "Arjun Reddy", "Bhavana Singh", "Chandana Naidu", "Deepak Kumar", 
    "Divya Reddy", "Ganesh Raju", "Ishani Sharma", "Jayaram Naidu", "Kavya Reddy", 
    "Krish Sharma", "Lavanya Naidu", "Madhav Kumar", "Meghana Reddy", "Nitin Raj", 
    "Pranav Kumar", "Prisha Sharma", "Rohini Naidu", "Samrat Reddy", "Sanvi Sharma", 
    "Siddharth Kumar", "Snehal Naidu", "Srinivas Raju", "Swathi Singh", "Tejas Reddy", 
    "Trisha Sharma", "Uday Kumar", "Vaishnavi Naidu", "Vijay Raju", "Yamini Singh", 
    "Abhinay Reddy", "Manideep Naidu", "Sonam Singh", "Priyanka Sharma", "Rahul Kumar", 
    "Ananya Reddy", "Akshay Naidu", "Anjali Singh", "Anurag Kumar", "Aarohi Sharma", 
    "Bhavna Reddy", "Chaitanya Naidu", "Deepika Singh", "Gaurav Kumar", "Haritha Naidu", 
    "Ishita Reddy", "Karthik Kumar", "Kavya Singh", "Krishna Naidu", "Lakshmi Singh", 
    "Manoj Kumar", "Meera Reddy", "Nandini Kumar", "Naveen Naidu", "Niharika Kumar", 
    "Nikhil Reddy", "Pooja Naidu", "Prakash Kumar", "Priya Reddy", "Rahul Kumar", 
    "Rajesh Naidu", "Rani Kumar", "Ravi Reddy", "Rishi Kumar", "Rohit Naidu", 
    "Sakshi Kumar", "Sameer Reddy", "Shilpa Naidu", "Shiva Kumar", "Shruti Reddy", 
    "Sneha Kumar", "Suman Naidu", "Suresh Kumar", "Tanvi Reddy", "Varun Kumar", 
    "Vikas Reddy", "Vinay Kumar", "Yash Naidu"
]

Places = ['Hyderabad', 'Hanamkonda', 'Warangal', 'Nagpur', 'Chandrapur', 'Mumbai', 'Delhi', 'KPHB', 'Secundrabad', 'uk']



def create_studnets():
    for i in range(145):
        if i < 50:
            standard = 8
            year = random.choice([2012,2013])
            last_two = str((i+1)%50)
            if len(last_two) == 1:
                last_two = '0' + last_two
            st_id = 'STU80'  + last_two
            login_id = 80000 + ((i + 1)%50)
            
        elif i < 100:
            standard = 9
            year = random.choice([2011,2012])
            last_two = str((i+1)%50)
            if len(last_two) == 1:
                last_two = '0' + last_two
            st_id = 'STU90'  + last_two
            login_id = 90000 + ((i + 1)%50)
        else:
            standard = 10
            year = random.choice([2010,2011])
            last_two = str((i+1)%50)
            if len(last_two) == 1:
                last_two = '0' + last_two
            st_id = 'STUX0'  + last_two
            login_id = 11000 + ((i + 1)%50)
        login_password = str(login_id) + student_names[i][:4]
        place = random.choice(Places)
        st = StudentLogin.objects.create(student_id = st_id, login_id = login_id,login_password = login_password)
        StudentDetails.objects.create(student_id = st,st_name = student_names[i],st_birth_year = year,st_birth_place = place,st_parent_name = Parents[i],st_standard = standard)




        