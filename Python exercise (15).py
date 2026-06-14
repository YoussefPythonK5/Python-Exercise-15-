# المستخدم يقول عنده عضويه ولا لا
membership = input("Do you have a membership? (yes/no): ")
# لو لا
if membership == "no":
	print ("Please create an account first")
# البرنامج بيطلب من المستخدم يكتب عمره
else:
	age = int(input ("How old are you?: "))
	if age >=18:
		print("Welcome! you can enter")
# لو أكبرمن أو يساوي 18 يطبع مرحبا تستطيع الدخول

# ولو المسخدم قال yes البرنامج هيسأله عن عمره ولو كان أكبر من او يساوي 18 البرنامج هيقوله مرحبا تستطيع الدخول