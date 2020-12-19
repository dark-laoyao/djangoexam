from django.shortcuts import render, redirect
from Grade_student.models import Grade, Student

def insert(request):
    g1 = Grade(g_name="大数据1班")
    g1.save()
    g2 = Grade(g_name="大数据2班")
    g2.save()
    g3 = Grade(g_name="大数据3班")
    g3.save()
    Student.objects.create(name="小王", email="wang@qq.com", password="123456", g=g1)
    Student.objects.create(name="李强", email="wang@qq.com", password="123456", g=g1)
    Student.objects.create(name="刘明", email="wang@qq.com", password="123456", g=g1)

    Student.objects.create(name="校长", email="wang@qq.com", password="123456", g=g2)
    Student.objects.create(name="小强", email="wang@qq.com", password="123456", g=g2)
    Student.objects.create(name="王强", email="wang@qq.com", password="123456", g=g2)

    Student.objects.create(name="熊大", email="wang@qq.com", password="123456", g=g3)
    Student.objects.create(name="熊二", email="wang@qq.com", password="123456", g=g3)
    Student.objects.create(name="光头强", email="wang@qq.com", password="123456", g=g3)
    return render(request, "insert.html")


def login(request):
    # un = list(Student.objects.all())
    # print(un, type(un))
    # for i in un:
    #     print(i)
    if request.method == "GET":
        return render(request,"login.html")
    else:
        name = request.POST.get("name")
        password = request.POST.get("password")
        un = Student.objects.filter(name=name, password=password).first()
        print(name, password, un)
        if un:
            if un:
                return redirect("show")
            # else:
            #     return "mimacuowu"
        else:
            return render(request, "login.html", {
                'nameorpassword': '用户名或密码错误'
            })


def show(request):
    s_all = Student.objects.all()
    if request.method == "GET":
        return render(request, "show.html" , {
            "s_all": s_all,
        })
    else:
        g_name = request.POST.get("g_name")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gb = Grade.objects.filter(g_name=g_name).first()
        if gb:
            Student.objects.create(name=name, email=email, password=password, g=gb)
        else:
            new_g = Grade(g_name=g_name)
            new_g.save()

            Student.objects.create(name=name, email=email, password=password, g=new_g)
        return redirect("show")



def delete(request, id):
    s = Student.objects.filter(id=id).first()
    if s:
        s.delete()
    return redirect("show")


def update(request, id):
    s = Student.objects.filter(id=id).first()
    if request.method == "GET":
        return render(request, "update.html", {"s":s})
    else:
        g_name = request.POST.get("g_name")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if name:
            s.name = name
        if email:
            s.email = email
        if password:
            s.password = password
        if g_name:
            gg = Grade.objects.filter(g_name=g_name).first()
            if gg:
                s.g = gg
            else:
                news_g = Grade(g_name=g_name)
                news_g.save()
                s.g = news_g
        s.save()
        return redirect("show")
# Create your views here.
