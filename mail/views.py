# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.shortcuts import render
# # Create your views here.
# def send_emails(request):
#     csv_file_path ="D:\PFSD\djangoproject\ttm\static\cs.csv"
#     with open("D:\PFSD\djangoproject\ttm\static\cs.csv", 'r') as csvfile:
#         reader = "D:\PFSD\djangoproject\ttm\static\cs.csv".DictReader(csvfile)
#         for row in reader:
#             recipient_email = row['email']
#             subject = 'Hello KLUian'  # Set your subject here
#             message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
#             send_mail(
#                 subject,
#                 message_body,
#
#                 [recipient_email],
#                 fail_silently=False,
#             )
#             print(f'Sent email to {recipient_email}')
#     return render(request, 'Emails_sent_successfully.html')