from django.shortcuts import render,redirect,HttpResponse
from login import models
from django.views.decorators.csrf import csrf_exempt
import json

def login(request):
    # import datetime
    # cur_time=datetime.datetime.now()
    # if request.method=="POST":
    #     _username=request.POST['username']
    #     _password=request.POST['passwd']
    #     if _username == '' or _password == '':
    #         errorInfo = 'alert("用户名和密码不能为空")'
    #         return render(request,"index.html",locals())
    #
    #     if models.userInfo.objects.filter(userId=_username).exists():
    #     # if models.userInfo.objects.filter(userName=_username).exists():
    #         obj=models.userInfo.objects.filter(userId=_username).values()[0]
    #         if _password==obj['userPassword']:
    #             name=obj['userName']
    #
    #             request.session['is_login'] = 'true'
    #             request.session['username']=name
    #             return redirect("/home"+str(obj['userIdentity'])+"/",locals())
    #             # return render(request,"home"+str(obj['userIdentity'])+".html",locals())
    #         else:
    #             errorInfo='alert("密码错误")'
    #             return render(request,"index.html",locals())
    #     else:
    #         errorInfo='alert("用户名不存在")'
    #         return render(request,"index.html",locals())
    # return render(request,"index.html",{'cur_time':cur_time})
    pass


def index(request):
    import datetime
    cur_time=datetime.datetime.now()
    if request.method == "POST":
        _username = request.POST['username']
        _password = request.POST['passwd']
        if _username == '' or _password == '':
            errorInfo = 'alert("用户名和密码不能为空")'
            return render(request,"index.html",locals())
        if models.userInfo.objects.filter(userId=_username).exists():
            obj = models.userInfo.objects.filter(userId=_username).values()[0]
            if _password == obj['userPassword']:
                name = obj['userName']
                user_identity = obj["userIdentity"]
                user_id = obj["userId"]
                request.session['is_login'] = 'true'
                request.session['username'] = name
                request.session['user_identity'] = user_identity
                request.session['user_id'] = user_id
                is_login = request.session['is_login']
                return redirect("/index2/",locals())
            else:
                errorInfo='alert("密码错误")'
                return render(request,"index.html",locals())
        else:
            errorInfo='alert("用户名不存在")'
            return render(request,"index.html",locals())
    return render(request,"index.html",{'cur_time':cur_time})


def index2(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_identity = request.session.get("user_identity")
        return render(request,'index2.html',locals())
    else:
        return render(request,"index.html")


def check_id_ajax(request):
    if request.method=="POST":
        print(request.POST)
        user_id=request.POST["user_id"]
        obj=models.userInfo.objects.filter(userId=user_id)
        print(obj)
        if obj.exists():
            info=["0"]
            userName=obj.values()[0]["userName"]
            info.append(userName)
            print(info)
            return HttpResponse(json.dumps(info))
        else:
            info = ["1"]
            return HttpResponse(json.dumps(info))
    else:
        return redirect("/keyan/")


def check_new_id_ajax(request):
    if request.method=="POST":
        user_id = request.POST["user_id"]
        if user_id.isdigit():
            obj = models.userInfo.objects.filter(userId=user_id)
            if obj.exists():
                info = ["0"]
                obj=obj.values()[0]
                user_info={
                    "user_name":obj["userName"],
                    "user_sex":obj["userSex"],
                    "user_edu_back":obj["userEduBack"],
                    "user_tech_post":obj["userTechPost"],
                }
                info.append(user_info)
                print(info)
                return HttpResponse(json.dumps(info))
            else:
                info = ["1"]
                return HttpResponse(json.dumps(info))
        else:
            info = ["2"]
            return HttpResponse(json.dumps(info))
    else:
        return redirect("/keyan/")


def keyan(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        obj_ = models.userInfo.objects.filter(userName=username).values()[0]
        user_identity = obj_["userIdentity"]
        user_id = obj_["userId"]
        obj = models.taskInfo.objects.filter(if_ratify=1).values().order_by("task_id")
        info_list = []
        for i in obj:
            i["principle_id"]=models.userInfo.objects.filter(userId=i["principle_id"]).values()[0]["userName"]
            info_list.append(i)
        return render(request,"keyan.html",locals())
        # else:
        #     info_list = []
        #     # list_1 = []
        #     # list_2 = []
        #     # obj = models.taskInfo.objects.all().values().order_by("task_id")
        #     # for i in obj:
        #     #     list_1.append(i)
        #     obj1=models.task_user.objects.filter(user_id=user_id).order_by("task_id").values()
        #
        #     for i in obj1:
        #         obj2=models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
        #         info_list.append(obj2)
        #     print(info_list)
        #     return render(request, "keyan.html", locals())
    else:
        return redirect("/index/")


def keyan_participate(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        obj_ = models.userInfo.objects.filter(userName=username).values()[0]
        print(obj_)
        user_identity = obj_["userIdentity"]
        user_id = obj_["userId"]
        info_list_1 = []
        info_list_2 = []
        obj0=models.taskInfo.objects.filter(principle_id=user_id).filter(if_ratify=1).order_by("task_id").values()
        obj1=models.task_user.objects.filter(user_id=user_id).order_by("task_id").values()
        for i in obj0:
            i["principle_id"]=models.userInfo.objects.filter(userId=i["principle_id"]).values()[0]["userName"]
            info_list_1.append(i)
        for i in obj1:
            obj2=models.taskInfo.objects.filter(task_id=i["task_id"]).filter(if_ratify=1)
            if obj2.exists():
                obj2=obj2.values()[0]
                obj2["principle_id"]=models.userInfo.objects.filter(userId=obj2["principle_id"]).values()[0]["userName"]
                info_list_2.append(obj2)
        if len(info_list_1) == 0:
            info_list_1.append("empty")
        if len(info_list_2) == 0:
            info_list_2.append("empty")
        return render(request, "keyan_participate.html", locals())
    else:
        return redirect("/index/")


def detail_info(req):
    if req.method=="POST":
        task_id = req.POST["task_id"]
        req.session['task_id']=task_id
        username = req.session.get('username')
        user_identity = req.session.get("user_identity")
        obj1=models.taskInfo.objects.filter(task_id=task_id).values()[0]
        principle_name=models.userInfo.objects.filter(userId=obj1["principle_id"]).values()[0]["userName"]
        task_info={"task_category":obj1["task_category"],
                   "task_name":obj1["task_name"],
                   "task_rank":obj1["task_rank"],
                   "principle_id":principle_name,
                   "task_id":obj1["task_id"],
                   }
        # task_info["principle_id"]=principle_name
        obj2=models.task_user.objects.filter(task_id=task_id).order_by("order").values()
        user_list = []
        for i in obj2:
            user_id = i["user_id"]
            order = i["order"]
            user = models.userInfo.objects.filter(userId=user_id).values()[0]
            dic = {"order":order,
                   "username":user["userName"],
                   "sex":user["userSex"],
                   "userEduBack":user["userEduBack"],
                   "userTechPost":user["userTechPost"],
                   }
            user_list.append(dic)
        info = [task_info,user_list,user_identity]
        return HttpResponse(json.dumps(info))
    else:
        return redirect("/keyan/")


def modify_ajax(req):
    if req.method=="POST":
        task_id = req.POST["task_id"]
        req.session['task_id']=task_id
        username = req.session.get('username')
        obj1=models.taskInfo.objects.filter(task_id=task_id).values()[0]
        principle_name=models.userInfo.objects.filter(userId=obj1["principle_id"]).values()[0]["userName"]
        task_info={"task_category":obj1["task_category"],
                   "task_name":obj1["task_name"],
                   "task_rank":obj1["task_rank"],
                   "principle_id":obj1["principle_id"],
                   "principle_name":principle_name,
                   "task_id":obj1["task_id"],
                   }
        # task_info["principle_id"]=principle_name
        obj2=models.task_user.objects.filter(task_id=task_id).order_by("order").values()
        user_list = []
        for i in obj2:
            user_id = i["user_id"]
            order = i["order"]
            user = models.userInfo.objects.filter(userId=user_id).values()[0]
            dic = {"order":order,
                   "user_id":user["userId"],
                   "username":user["userName"],
                   "sex":user["userSex"],
                   "userEduBack":user["userEduBack"],
                   "userTechPost":user["userTechPost"],
                   }
            user_list.append(dic)
        info = [task_info,user_list]
        return HttpResponse(json.dumps(info))
    else:
        return redirect("/keyan/")


def task_modify(request):
    if request.method == "POST":
        task_id = request.session.get('task_id')
        models.task_user.objects.filter(task_id=task_id).delete()
        print(request.POST)
        member_list_length=len(request.POST)-5
        for i in range(member_list_length):
            print(request.POST[str(i+1)])
            models.task_user.objects.create(**{
                "task_id": task_id,
                "order": i+1,
                "user_id": request.POST[str(i+1)],
            })
        obj=models.taskInfo.objects.filter(task_id=task_id)
        obj.update(task_name=request.POST["task_name"])
        obj.update(principle_id=request.POST["principle_id"])
        obj.update(task_category=request.POST["task_category"])
        obj.update(task_rank=request.POST["task_rank"])
        return redirect("/keyan_participate/")
    else:
        return redirect("/keyan_participate/")


def add_task_member(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        if request.method=="POST":
            task_member = request.POST["add_task_member"]
            if models.userInfo.objects.filter(userId=task_member).exists():
                task_id=request.session.get("task_id")
                order=models.task_user.objects.filter(task_id=task_id).order_by("order").reverse().values()
                order=order[0]["order"]+1
                print(order)
                models.task_user.objects.create(**{"task_id": task_id,
                                                  "order": order,
                                                  "user_id": task_member,
                                                  })
                return redirect("/keyan/")
    else:
        return redirect("/index/")


def keyan_add_task(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        if request.method=="POST":
            print(request.POST)
            task_name=request.POST["task_name"]
            principle_id=request.POST["principle_id"]
            task_category=request.POST["task_category"]
            task_rank=request.POST["task_rank"]
            budget_remaining=budget_total=request.POST["budget_total"]
            print(budget_total)
            if task_name == '' or principle_id == "":
                errorInfo = 'alert("项目名和负责人不能为空")'
                return render(request, "keyan_add_task.html", locals())
            else:
                models.taskInfo.objects.create(**{"task_name": task_name,
                                                  "principle_id": principle_id,
                                                  "task_category": task_category,
                                                  "task_rank":task_rank,
                                                  })
                task_id=models.taskInfo.objects.filter(task_name=task_name).values()[0]["task_id"]
                models.task_user.objects.create(**{"task_id":task_id,
                                                   "user_id":principle_id,
                                                   "order":1,})
                models.budget.objects.create(**{
                    "task_id":task_id,
                    "total":budget_total,
                    "remaining":budget_remaining,
                })
                return redirect("/keyan/")
        else:
            username = request.session.get('username')
            user_identity = models.userInfo.objects.filter(userName=username).values()[0]['userIdentity']
            return render(request, "keyan_add_task.html", locals())
    else:
        return redirect("/index/")


def keyan_ratify(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        obj1 = models.taskInfo.objects.filter(if_ratify=0).order_by("task_id").values()
        info_list_1 = []
        for i in obj1:
            obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
            i["principle_id"] = models.userInfo.objects.filter(userId=i["principle_id"]).values()[0]["userName"]
            info_list_1.append(i)
        obj3 = models.taskInfo.objects.filter(if_ratify=2).order_by("task_id").values()
        info_list_2 = []
        for i in obj3:
            obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
            i["principle_id"] = models.userInfo.objects.filter(userId=i["principle_id"]).values()[0]["userName"]
            info_list_2.append(i)
        return render(request, "keyan_ratify.html", locals())
    else:
        return redirect("/index/")


def keyan_except(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        return render(request,"keyan_except.html",locals())
    else:
        return redirect("/index/")


def keyan_if_ratify_ajax(request):
    if request.method=="POST":
        task_id = request.POST["task_id"]
        flag = int(request.POST["if_ratify"])
        if flag == 1:
            obj = models.taskInfo.objects.filter(task_id=task_id)
            obj.update(if_ratify=1)
        elif flag == 2:
            obj = models.taskInfo.objects.filter(task_id=task_id)
            obj.update(if_ratify=2)
        return HttpResponse("ok")
    else:
        return redirect("/keyan_ratify/")


def achievement(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        obj1=models.JournalArticle.objects.all().values()
        info_list_1=[]
        for i in obj1:
            i["author_id"] = models.userInfo.objects.filter(userId=i["author_id"]).values()[0]["userName"]
            i["task_id"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            info_list_1.append(i)
        obj2 = models.Patent.objects.all().values()
        info_list_2 = []
        for i in obj2:
            i["author_id"] = models.userInfo.objects.filter(userId=i["author_id"]).values()[0]["userName"]
            i["task_id"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            info_list_2.append(i)
        obj3 = models.ConferenceArticle.objects.all().values()
        info_list_3 = []
        for i in obj3:
            i["author_id"] = models.userInfo.objects.filter(userId=i["author_id"]).values()[0]["userName"]
            i["task_id"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            info_list_3.append(i)
        obj4 = models.AcademicMonograph.objects.all().values()
        info_list_4 = []
        for i in obj4:
            i["author_id"] = models.userInfo.objects.filter(userId=i["author_id"]).values()[0]["userName"]
            i["task_id"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            info_list_4.append(i)
        obj5 = models.SoftwarePatent.objects.all().values()
        info_list_5 = []
        for i in obj5:
            i["author_id"] = models.userInfo.objects.filter(userId=i["author_id"]).values()[0]["userName"]
            i["task_id"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            info_list_5.append(i)
        return render(request,"achievement.html",locals())
    else:
        return redirect("/index/")


def journal_article_ajax(request):
    if request.method=="POST":
        achievement_id=request.POST["id"]
        obj=models.JournalArticle.objects.filter(id=achievement_id).values()[0]
        obj["author_id"]=models.userInfo.objects.filter(userId=obj["author_id"]).values()[0]["userName"]
        obj["task_id"]=models.taskInfo.objects.filter(task_id=obj["task_id"]).values()[0]["task_name"]
        print(obj)
        return HttpResponse(json.dumps(obj))
    else:
        return redirect("/achievement/")


def patent_ajax(request):
    if request.method=="POST":
        achievement_id=request.POST["id"]
        obj=models.Patent.objects.filter(id=achievement_id).values()[0]
        obj["author_id"]=models.userInfo.objects.filter(userId=obj["author_id"]).values()[0]["userName"]
        obj["task_id"]=models.taskInfo.objects.filter(task_id=obj["task_id"]).values()[0]["task_name"]
        print(obj)
        return HttpResponse(json.dumps(obj))
    else:
        return redirect("/achievement/")


def conference_article_ajax(request):
    if request.method=="POST":
        achievement_id=request.POST["id"]
        obj=models.ConferenceArticle.objects.filter(id=achievement_id).values()[0]
        obj["author_id"]=models.userInfo.objects.filter(userId=obj["author_id"]).values()[0]["userName"]
        obj["task_id"]=models.taskInfo.objects.filter(task_id=obj["task_id"]).values()[0]["task_name"]
        print(obj)
        return HttpResponse(json.dumps(obj))
    else:
        return redirect("/achievement/")


def academic_monograph_ajax(request):
    if request.method=="POST":
        achievement_id=request.POST["id"]
        obj=models.AcademicMonograph.objects.filter(id=achievement_id).values()[0]
        obj["author_id"]=models.userInfo.objects.filter(userId=obj["author_id"]).values()[0]["userName"]
        obj["task_id"]=models.taskInfo.objects.filter(task_id=obj["task_id"]).values()[0]["task_name"]
        print(obj)
        return HttpResponse(json.dumps(obj))
    else:
        return redirect("/achievement/")


def software_patent_ajax(request):
    if request.method=="POST":
        achievement_id=request.POST["id"]
        obj=models.SoftwarePatent.objects.filter(id=achievement_id).values()[0]
        obj["author_id"]=models.userInfo.objects.filter(userId=obj["author_id"]).values()[0]["userName"]
        obj["task_id"]=models.taskInfo.objects.filter(task_id=obj["task_id"]).values()[0]["task_name"]
        print(obj)
        return HttpResponse(json.dumps(obj))
    else:
        return redirect("/achievement/")

def add_achievement(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        if request.method=="POST":
            print(request.POST)
            flag=int(request.POST["add_category"])
            if flag==1:
                models.JournalArticle.objects.create(**{
                    "title":request.POST["title"],
                    "author_id":user_id,
                    "journal_name":request.POST["journal_name"],
                    "publish_time":request.POST["publish_time"],
                    "roll_num":request.POST["roll_num"],
                    "start_end_page":request.POST["start_end_page"],
                    "task_id":request.POST["task_id"],
                })
                return render(request,"achievement.html",locals())
            if flag==2:
                models.Patent.objects.create(**{
                    "patent_name":request.POST["patent_name"],
                    "author_id":user_id,
                    "country":request.POST["country"],
                    "patent_num":request.POST["patent_num"],
                    "institution":request.POST["institution"],
                    "category":request.POST["category"],
                    "status":request.POST["status"],
                    "apply_for_time":request.POST["apply_for_time"],
                    "take_effect_time":request.POST["take_effect_time"],
                    "task_id":request.POST["task_id"],
                })
                return render(request,"achievement.html",locals())
            if flag==3:
                models.ConferenceArticle.objects.create(**{
                    "article_title":request.POST["article_title"],
                    "author_id":user_id,
                    "category":request.POST["category"],
                    "confer_name":request.POST["confer_name"],
                    "confer_time":request.POST["confer_time"],
                    "publish_time":request.POST["publish_time"],
                    "area":request.POST["area"],
                    "task_id":request.POST["task_id"],
                })
                return render(request,"achievement.html",locals())
            if flag==4:
                models.AcademicMonograph.objects.create(**{
                    "title":request.POST["title"],
                    "author_id":user_id,
                    "editor": request.POST["editor"],
                    "area": request.POST["area"],
                    "publish_time": request.POST["publish_time"],
                    "publisher": request.POST["publisher"],
                    "task_id": request.POST["task_id"],
                })
                return render(request,"achievement.html",locals())
            if flag==5:
                models.SoftwarePatent.objects.create(**{
                    "name":request.POST["name"],
                    "author_id":user_id,
                    "register_num": request.POST["register_num"],
                    "method": request.POST["method"],
                    "finish_time": request.POST["finish_time"],
                    "task_id": request.POST["task_id"],

                })
                return render(request,"achievement.html",locals())
        return render(request,"add_achievement.html",locals())
    else:
        return redirect("/index/")


#performance页面的首页
def performance(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        obj=models.taskInfo.objects.filter(if_ratify=1).values()
        info_list=[]
        for i in obj:
            i["principle_id"]=models.userInfo.objects.filter(userId=i["principle_id"]).values()[0]["userName"]
            info_list.append(i)
        return render(request,"performance.html",locals())
    else:
        return redirect("/index/")


def performance_ajax(request):
    if request.method=="POST":
        task_id=request.POST["task_id"]
        obj=models.taskInfo.objects.filter(task_id=task_id).values()[0]
        obj["principle_id"]=models.userInfo.objects.filter(userId=obj["principle_id"]).values()[0]["userName"]
        obj1=models.JournalArticle.objects.filter(task_id=task_id).values()
        obj2=models.Patent.objects.filter(task_id=task_id).values()
        obj3=models.ConferenceArticle.objects.filter(task_id=task_id).values()
        obj4=models.AcademicMonograph.objects.filter(task_id=task_id).values()
        obj5=models.SoftwarePatent.objects.filter(task_id=task_id).values()
        num_list=[obj,[len(obj1),len(obj2),len(obj3),len(obj4),len(obj5),]]
        print(num_list)
        return HttpResponse(json.dumps(num_list))
    else:
        return redirect("/achievement/")


#information页面的首页
def information(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        if True:
            obj1 = models.userInfo.objects.all().order_by("userId").values()
            user_info_list=[]
            for i in obj1:
                user_info_list.append(i)
            print(user_info_list[0])
            return render(request,"information.html",locals())
        # elif user_identity==1:
        #     obj2 = models.teacher_student.objects.filter(teacher=user_id).order_by("student").values()
        #     user_info_list=[models.userInfo.objects.filter(userId=user_id).values()[0], ]
        #     print(user_info_list)
        #     for i in obj2:
        #         stu_info = models.userInfo.objects.filter(userId=i["student"]).values()[0]
        #         print(stu_info)
        #         user_info_list.append(stu_info)
        #     return render(request,"information.html",locals())
        # elif user_identity==2:
        #     obj3 = models.teacher_student.objects.filter(student=user_id).values()[0]
        #     teacher = obj3["teacher"]
        #     user_info_list = [models.userInfo.objects.filter(userId=teacher).values()[0], ]
        #     obj4 = models.teacher_student.objects.filter(teacher=teacher).order_by("student").values()
        #     for i in obj4:
        #         stu_info = models.userInfo.objects.filter(userId=i["student"]).values()[0]
        #         print(stu_info)
        #         user_info_list.append(stu_info)
        #     return render(request,"information.html",locals())
    else:
        return redirect("/index/")


def info_team(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        if user_identity == 1:
            obj2 = models.teacher_student.objects.filter(teacher=user_id).order_by("student").values()
            user_info_list = [models.userInfo.objects.filter(userId=user_id).values()[0], ]
            print(user_info_list)
            for i in obj2:
                stu_info = models.userInfo.objects.filter(userId=i["student"]).values()[0]
                print(stu_info)
                user_info_list.append(stu_info)
            return render(request, "info_team.html", locals())

        elif user_identity == 2:
            obj3 = models.teacher_student.objects.filter(student=user_id).values()[0]
            teacher = obj3["teacher"]
            user_info_list = [models.userInfo.objects.filter(userId=teacher).values()[0], ]
            obj4 = models.teacher_student.objects.filter(teacher=teacher).order_by("student").values()
            for i in obj4:
                stu_info = models.userInfo.objects.filter(userId=i["student"]).values()[0]
                print(stu_info)
                user_info_list.append(stu_info)
            return render(request, "info_team.html", locals())


#添加新用户
def info_add_user(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        if request.method=="POST":
            print("123")
            userName=request.POST["userName"]
            userSex=request.POST["userSex"]
            userEduBack=request.POST["userEduBack"]
            userTechPost=request.POST["userTechPost"]
            userIdentity=request.POST["userIdentity"]
            userId = models.userInfo.objects.filter(userIdentity=userIdentity).order_by("userId").reverse()
            userId = userId.values()[0]["userId"] + 1
            # print(userId)
            models.userInfo.objects.create(**{"userName": userName,
                                              "userPassword": "123456",
                                              "userTechPost": userTechPost,
                                              "userEduBack": userEduBack,
                                              "userId": userId,
                                              "userSex": userSex,
                                              "userIdentity": userIdentity,
                                                  })
            return redirect("/information/")
        return render(request,"info_add_user.html",locals())
    else:
        return redirect("/index/")


#添加项目组成员
def add_group_member(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        if request.method == "POST":
            print("123")
            teacher = request.session.get("user_id")
            student = request.POST["add_group_member"]
            models.teacher_student.objects.create(**{"teacher":teacher,
                                                     "student":student})
    return redirect("/information/")


# 修改密码
def change_password_ajax(request):
    pass

# 修改密码
def change_password(request):
    is_login = request.session.get('is_login', False)
    username = request.session.get('username')
    user_id = request.session.get("user_id")
    user_identity = request.session.get("user_identity")
    if is_login:
        if request.method == "POST":
            old_passwd=request.POST["old_passwd"]
            new_passwd_1 = request.POST["new_passwd_1"]
            new_passwd_2 = request.POST["new_passwd_2"]
            obj = models.userInfo.objects.filter(userId=user_id)
            raw_passwd=obj.values()[0]["userPassword"]
            if new_passwd_1==new_passwd_2:
                print("123")
                if old_passwd==raw_passwd:
                    print("456")
                    obj.update(userPassword=new_passwd_1)
                    return redirect("/logout/")
                else:
                    errorInfo='alert("旧密码输入错误")'
                    return render(request, "change_passwd.html", locals())
            else:
                errorInfo = 'alert("两次密码输入不一致")'
                return render(request,"change_passwd.html",locals())
        return render(request,"change_passwd.html",locals())
    return redirect("/index/")


def budget(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        # username = request.session.get('username')
        # user_id = request.session.get("user_id")
        # user_identity = request.session.get("user_identity")
        # return render(request,"budget.html",locals())
        username = request.session.get('username')
        obj_ = models.userInfo.objects.filter(userName=username).values()[0]
        print(obj_)
        user_identity = obj_["userIdentity"]
        user_id = obj_["userId"]
        if user_identity == 0:
            obj = models.taskInfo.objects.all().values().order_by("task_id")
            info_list = []
            for i in obj:
                info_list.append(i)
            return render(request, "budget.html", locals())
        else:
            obj1 = models.task_user.objects.filter(user_id=user_id).order_by("task_id").values()
            info_list = []
            for i in obj1:
                obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
                info_list.append(obj2)
            print(info_list)
            return render(request, "budget.html", locals())
    else:
        return redirect("/index/")


def detail_budget_ajax(req):
    if req.method=="POST":
        task_id = req.POST["task_id"]
        req.session['task_id']=task_id
        username = req.session.get('username')
        user_identity = req.session.get("user_identity")
        obj1=models.taskInfo.objects.filter(task_id=task_id).values()[0]
        obj2=models.budget.objects.filter(task_id=task_id).values()[0]
        # print(obj2)
        principle_name=models.userInfo.objects.filter(userId=obj1["principle_id"]).values()[0]["userName"]
        b1=float(obj2["b1_1"])+float(obj2["b1_2"])+float(obj2["b1_3"])
        task_info={
            "task_name":obj1["task_name"],
            "principle_id":principle_name,
            "task_id":obj1["task_id"],
            "b1_1":obj2["b1_1"],
            "b1_2":obj2["b1_2"],
            "b1_3":obj2["b1_3"],
            "b1":b1,
            "b2":obj2["b2"],
            "b3":obj2["b3"],
            "b4":obj2["b4"],
            "b5":obj2["b5"],
            "b6":obj2["b6"],
            "b7":obj2["b7"],
            "b8":obj2["b8"],
            "b9":obj2["b9"],
            "remaining":obj2["remaining"],
            "total":obj2["total"],
        }
        # task_info["principle_id"]=principle_name
        obj2=models.budget_out.objects.filter(task_id=task_id).values()
        user_list = []
        for i in obj2:
            user_id = i["user_id"]
            user = models.userInfo.objects.filter(userId=user_id).values()[0]
            dic = {"username":user["userName"],
                   "number":i["number"],
                   "to_credit_card":i["to_credit_card"],
                   "type":i["type"],
                   }
            if i["type"] == "b1_1":
                dic["type"] = "设备购置费"
            elif i["type"] == "b1_2":
                dic["type"] = "设备试制费"
            elif i["type"] == "b1_3":
                dic["type"] = "设备改造与租赁费"
            elif i["type"] == "b2":
                dic["type"] = "材料费"
            elif i["type"] == "b3":
                dic["type"] = "测试化加工费"
            elif i["type"] == "b4":
                dic["type"] = "燃料动力费"
            elif i["type"] == "b5":
                dic["type"] = "差旅/会议/国际合作与交流费"
            elif i["type"] == "b6":
                dic["type"] = "出版 / 文献 / 信息传播 / 知识产权事务费"
            elif i["type"] == "b7":
                dic["type"] = "劳务费"
            elif i["type"] == "b8":
                dic["type"] = "专家咨询费"
            elif i["type"] == "b9":
                dic["type"] = "其他支出"
            # print(dic)
            user_list.append(dic)
        info = [task_info,user_list,user_identity]
        return HttpResponse(json.dumps(info))
    else:
        return redirect("/budget/")


def budget_out(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get('user_id')
        user_identity = request.session.get("user_identity")
        info_list = []
        obj1 = models.task_user.objects.filter(user_id=user_id).order_by("task_id").values()
        for i in obj1:
            obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
            info_list.append(obj2)
        # print(info_list)
        if request.method=="POST":
            task_id = request.POST["task_id"]
            # print(request.POST["task_id"])
            number = request.POST["number"]
            to_credit_card = request.POST["to_credit_card"]
            type = "".join(["b",request.POST["type"]])
            obj = models.budget.objects.filter(task_id=task_id).values()[0]
            remaining = float(obj["remaining"])
            number = float(number)
            # print(remaining)
            if remaining>number:
                models.budget_out.objects.create(**{
                    "task_id":task_id,
                    "user_id":user_id,
                    "number":number,
                    "to_credit_card":to_credit_card,
                    "type":type,
                })
                remaining = remaining - number
                obj2 = models.budget.objects.filter(task_id=task_id)
                obj2.update(remaining=remaining)
                obj3=obj2.values()[0]
                if type == "b1_1":
                    b1_1 = float(obj3["b1_1"])
                    b1_1 += number
                    print(b1_1)
                    obj2.update(b1_1=b1_1)
                elif type == "b1_2":
                    b1_2 = float(obj3["b1_2"])
                    b1_2 += number
                    obj2.update(b1_2=b1_2)
                elif type == "b1_3":
                    b1_3 = float(obj3["b1_3"])
                    b1_3 += number
                    obj2.update(b1_3=b1_3)
                elif type == "b2":
                    b2 = float(obj3["b2"])
                    b2 += number
                    obj2.update(b2=b2)
                elif type == "b3":
                    b3 = float(obj3["b3"])
                    b3 += number
                    obj2.update(b3=b3)
                elif type == "b4":
                    b4 = float(obj3["b4"])
                    b4 += number
                    obj2.update(b4=b4)
                elif type == "b5":
                    b5 = float(obj3["b5"])
                    b5 += number
                    obj2.update(b5=b5)
                elif type == "b6":
                    b6 = float(obj3["b6"])
                    b6 += number
                    obj2.update(b6=b6)
                elif type == "b7":
                    b7 = float(obj3["b7"])
                    b7 += number
                    obj2.update(b7=b7)
                elif type == "b8":
                    b8 = float(obj3["b8"])
                    b8 += number
                    obj2.update(b8=b8)
                elif type == "b9":
                    b9 = float(obj3["b9"])
                    b9 += number
                    obj2.update(b9=b9)
                return redirect("/budget/")
            else:
                errorInfo = 'alert("经费余额不足！")'
                return render(request,"budget_out.html",locals())
        else:
            return render(request,"budget_out.html",locals())
    else:
        return redirect("/login/")


def property(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        if user_identity == 0:
            obj1 = models.purchase.objects.filter(if_ratify=0).order_by("id").values()
            info_list_1=[]
            for i in obj1:
                obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
                i["task_name"] = obj2["task_name"]
                info_list_1.append(i)
            obj3 = models.purchase.objects.filter(if_ratify=2).order_by("id").values()
            info_list_2 = []
            for i in obj3:
                obj4 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
                i["task_name"] = obj4["task_name"]
                info_list_2.append(i)
            return render(request, "property.html", locals())
        else:
            obj1 = models.purchase.objects.filter(proposer=user_id).order_by("if_ratify").values()
            info_list = []
            for i in obj1:
                dic={
                    "id":i["id"],
                    "name":i["property_name"],
                    "if_ratify":i["if_ratify"],
                }
                obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
                dic["task_name"]=obj2["task_name"]
                info_list.append(dic)
            return render(request,"property.html",locals())
    else:
        return redirect("/index/")


def pro_purchase(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        obj1 = models.task_user.objects.filter(user_id=user_id).order_by("task_id").values()
        info_list = []
        for i in obj1:
            obj2 = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]
            info_list.append(obj2)
        if request.method=="POST":
            property_name = request.POST["property_name"]
            print(request.POST)
            detail_info = request.POST["detail_info"]
            price = request.POST["price"]
            task_id = request.POST["task_id"]
            models.purchase.objects.create(**{
                "proposer": user_id,
                "property_name": property_name,
                "detail_info": detail_info,
                "task_id": task_id,
                "price": price,
                "if_ratify": 0,
            })
            return redirect("/property/")
        return render(request,"pro_purchase.html",locals())
    else:
        return redirect("/index/")


def if_ratify(request):
    if request.method == "POST":
        property_id = request.POST["property_id"]
        flag = int(request.POST["if_ratify"])
        import time
        if flag == 1:
            obj = models.purchase.objects.filter(id=property_id)
            obj.update(if_ratify=1)
            obj = obj.values()[0]
            times = time.strftime("%Y-%m-%d %X", time.localtime())
            models.property.objects.create(**{
                "price": obj["price"],
                "proposer": obj["proposer"],
                "property_name": obj["property_name"],
                "purchase_time": times,
                "status": 0,
                "task_id": obj["task_id"],
            })
            price = obj["price"]
            to_credit_card = "资产管理"
            type = "b1_1"
            user_id = obj["proposer"]
            obj = models.budget.objects.filter(task_id=obj["task_id"]).values()[0]
            remaining = float(obj["remaining"])
            price = float(price)/10000
            # print(remaining)
            if remaining > price:
                models.budget_out.objects.create(**{
                    "task_id": obj["task_id"],
                    "user_id": user_id,
                    "number": price,
                    "to_credit_card": to_credit_card,
                    "type": type,
                })
                remaining = remaining - price
                obj2 = models.budget.objects.filter(task_id=obj["task_id"])
                obj2.update(remaining=remaining)
                obj3 = obj2.values()[0]
                b1_1 = float(obj3["b1_1"])
                b1_1 += price
                print(b1_1)
                obj2.update(b1_1=b1_1)
        elif flag == 2:
            obj = models.purchase.objects.filter(id=property_id)
            obj.update(if_ratify=2)
        return HttpResponse("ok")
    else:
        return redirect("/property/")


def property_all(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        info_list = []
        '''
        <td>{{ i.id }}</td>
                <td>{{ i.property_name }}</td>
                <td>{{ i.proposer }}</td>
                <td>{{ i.price }}</td>
                <td>{{ i.purchase_time }}</td>
                <td>{{ i.scrap_time }}</td>
                <td>{{ i.task_name }}</td>
                <td>{{ i.status }}</td>
        '''
        obj = models.property.objects.all().order_by("status").values()
        for i in obj:
            i["task_name"]=models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            i["proposer"]=models.userInfo.objects.filter(userId=i["proposer"]).values()[0]["userName"]
            flag = i["status"]
            if flag == 0:
                i["status"]="正常使用"
            elif flag == 1:
                i["status"] = "申请报废"
            elif flag == 2:
                i["status"] = "已报废"
            info_list.append(i)
        return render(request,"property_all.html",locals())
    else:
        return redirect("/index/")


def property_baofei(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        username = request.session.get('username')
        user_id = request.session.get("user_id")
        user_identity = request.session.get("user_identity")
        obj = models.property.objects.filter(status=0).order_by("status").values()
        info_list=[]
        for i in obj:
            i["task_name"] = models.taskInfo.objects.filter(task_id=i["task_id"]).values()[0]["task_name"]
            i["proposer"] = models.userInfo.objects.filter(userId=i["proposer"]).values()[0]["userName"]
            flag = i["status"]
            if flag == 0:
                i["status"] = "正常使用"
            elif flag == 1:
                i["status"] = "申请报废"
            elif flag == 2:
                i["status"] = "已报废"
            info_list.append(i)
        return render(request, "property_baofei.html", locals())
    else:
        return redirect("/index/")


def scrap_ajax(request):
    if request.method=="POST":
        property_id = request.POST["property_id"]
        import time
        obj = models.property.objects.filter(id=property_id)
        times = time.strftime("%Y-%m-%d %X", time.localtime())
        obj.update(status=2)
        obj.update(scrap_time=times)
        return HttpResponse("ok")
    else:
        return redirect("/property/")


def logout(request):
    """
    直接通过request.session['is_login']回去返回的时候，
    如果is_login对应的value值不存在会导致程序异常。所以
    需要做异常处理
    """
    try:
        #删除is_login对应的value值
        del request.session['is_login']
    except KeyError:
        pass
    #点击注销之后，直接重定向回登录页面
    return redirect('/index/')


def test(request):
    if request.method=="POST":
        print(request.POST["test"])
        return render(request, "index.html", locals())
    return render(request, "test.html", locals())


