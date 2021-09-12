from flask import Flask,render_template,request,session,jsonify
from DBConnection import Db
app = Flask(__name__)
app.secret_key="abcc"

@app.route('/admin')
def admin():
    return render_template("admin/home.html")


@app.route('/adm_add_delivery_boy')
def adm_add_delivery_boy():
    return render_template("admin/add_delivery_boy.html")

@app.route('/adm_add_delivery_boy_post',methods=['post'])
def adm_add_delivery_boy_post():
    d = Db()
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    contact=request.form['contact']
    email=request.form['email']
    age=request.form['age']
    pic = request.files['img']
    pic.save("C:\\Users\\THIS PC\\PycharmProjects\\evengara\\static\\imgs\\deliveryboy\\"+pic.filename)
    path = "/static/imgs/deliveryboy/" + pic.filename
    qry1= "insert into login(username,password,usertype)values('"+ email +"','"+ contact +"','pending')"
    res1=d.insert(qry1)

    qry = "insert into deliveryboy(name,place,post,pin,age,email,contact,image,loginid)values('" + name + "','" + place + "','" + post + "','" + pin + "','" + age + "','" + email + "','" + contact + "','" + path + "','"+str(res1)+"')"
    res = d.insert(qry)
    return adm_add_delivery_boy()

@app.route('/adm_view_delivery_boy')
def adm_view_delivery_boy():
    r = Db()
    qry = "select * from deliveryboy"
    res = r.select(qry)
    return render_template("admin/view_delivery_boy.html",val=res)

@app.route('/adm_delete_delivery_boy/<id>')
def adm_delete_delivery_boy(id):
    r = Db()
    qry="delete from deliveryboy where boyid='"+id+"'"
    res = r.delete(qry)
    return adm_view_delivery_boy()

@app.route('/adm_delivery_boy_edit/<id>')
def adm_delivery_boy_edit(id):
    r = Db()
    qry = "select * from deliveryboy where boyid='" + id + "'"
    res= r.selectOne(qry)
    return render_template("admin/delivery_boy_edit.html",val=res)

@app.route('/adm_edit_delivery_boy_post',methods=['post'])
def adm_edit_delivery_boy_post():
    d = Db()
    boyid=request.form['boyid']
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    contact=request.form['contact']
    email=request.form['email']
    age=request.form['age']
    if "img" in request.files:

        pic =request.files['img']
        if pic.filename != "" :

            pic.save("C:\\Users\\THIS PC\\PycharmProjects\\evengara\\static\\imgs\\deliveryboy\\" + pic.filename)
            path = "/static/imgs/deliveryboy/" + pic.filename
            qry = "UPDATE deliveryboy SET name = '" + name + "', age = '" + age + "',place = '" + place + "',post = '" + post + "',pin= '" + pin + "',contact= '" + contact + "',email = '" + email + "',image = '" + path + "'  where boyid='" + boyid + "'"
            res = d.update(qry)
        else :
            qry = "UPDATE deliveryboy SET name = '" + name + "', age = '" + age + "',place = '" + place + "',post = '" + post + "',pin= '" + pin + "',contact= '" + contact + "',email = '" + email + "'  where boyid='" + boyid + "'"
            res = d.update(qry)
    else:
        qry = "UPDATE deliveryboy SET name = '" + name + "', age = '" + age + "',place = '" + place + "',post = '" + post + "',pin= '" + pin + "',contact= '" + contact + "',email = '" + email + "'  where boyid='" + boyid + "'"
        res = d.update(qry)


    return adm_view_delivery_boy()

@app.route('/adm_view_new_shop')
def adm_view_new_shop():
    r = Db()
    qry = "SELECT shop.* FROM shop,login WHERE shop.loginid = login.loginid AND login.usertype= 'pending'"
    res = r.select(qry)
    return render_template("admin/view_new_shop.html", val=res)

@app.route('/adm_approve_new_shop/<id>')
def adm_accept_new_shop(id):
    r = Db()
    qry = "UPDATE login SET usertype= 'shop' where loginid= '"+id+"'"
    res= r.update(qry)
    return adm_view_new_shop()


@app.route('/adm_reject_new_shop/<id>')
def adm_reject_new_shop(id):
    r = Db()
    qry = "UPDATE login SET usertype= 'reject' where loginid= '"+id+"'"
    res= r.update(qry)
    return adm_view_new_shop()

@app.route('/adm_view_accepted_shop')
def adm_view_accepted_shop():
    r = Db()
    qry = "SELECT shop.* FROM shop,login WHERE shop.loginid = login.loginid AND login.usertype= 'shop'"
    res = r.select(qry)
    return render_template("admin/view_accepted_shop.html", val=res)

@app.route('/adm_view_shop/<id>')
def adm_view_shop(id):
    d=Db()
    qry1="select * from shop where shopid='"+id+"'"
    res1=d.selectOne(qry1)

    qry2="select products.*,category.category from products,category where products.shopid='"+str(res1['loginid'])+"' and products.categoryid=category.cat_id"
    res2=d.select(qry2)
    qry3 = "SELECT review.*,customer.name AS cname FROM review,customer WHERE customer.loginid = review.userid AND review.type='shop' and review.id='"+id+"'"
    res3=d.select(qry3)
    return render_template("admin/view_shop.html",val=res1,data=res2,rew=res3)

@app.route('/adm_search_shop',methods=['post'])
def adm_search_shop():
    d = Db()
    search = request.form['search']
    qry= "SELECT * FROM shop WHERE NAME LIKE '%"+search+"%'"
    res=d.select(qry)
    return render_template("admin/view_accepted_shop.html", val=res)


@app.route('/adm_view_rejected_shop')
def adm_view_rejected_shop():
    r = Db()
    qry = "SELECT shop.* FROM shop,login WHERE shop.loginid = login.loginid AND login.usertype= 'reject'"
    res = r.select(qry)
    return render_template("admin/view_rejected_shop.html", val=res)

@app.route('/adm_approve_rejected_shop/<id>')
def adm_approve_rejected_shop(id):
    r = Db()
    qry = "UPDATE login SET usertype= 'shop' where loginid= '" + id + "'"
    res = r.update(qry)
    return admin()
@app.route('/adm_view_and_search_customer')
def adm_view_and_search_customer():
    r=Db();
    qry = "SELECT * FROM customer"
    res=r.select(qry)
    return render_template("admin/view_and_search_customer.html",val=res)

@app.route('/adm_search_customer',methods=['post'])
def adm_search_customer():
    d = Db()
    search = request.form['search']
    qry= "SELECT * FROM customer WHERE NAME LIKE '%"+search+"%'"
    res=d.select(qry)
    return render_template("admin/view_and_search_customer.html", val=res)

# @app.route('/adm_view_reviews')
# def adm_view_reviews():
#     r = Db();
#     qry = "SELECT review.*,customer.name AS cname,shop.name as shopname FROM review,customer,shop WHERE customer.loginid = review.userid AND shop.loginid = review.shopid"
#     res = r.select(qry)
#     return render_template("admin/view_reviews.html",val=res)



@app.route('/adm_change_password')
def adm_change_password():
    return render_template("admin/change_password.html")

@app.route('/adm_change_pass_post',methods=['post'])
def adm_change_pass_post():
    d=Db()
    cur_pass=request.form['cur_pass']
    new_pass = request.form['new_pass']
    confirm_pass = request.form['confirm_pass']
    qry="select password from login where loginid=1"
    res=d.selectOne(qry)
    if str(res['password']) == cur_pass:
        if new_pass == confirm_pass:
            qry2="update login set password='"+new_pass+"' where loginid=1"
            res2=d.insert(qry2)
        else:
            return ("password not match")
    else:
        return ("please enter correct password")
    return render_template("admin/home.html")

@app.route('/')
def adm_login():

    return render_template("admin/login.html")


@app.route('/adm_login_post',methods=['post'])
def adm_login_post():
    username= request.form['username']
    password= request.form['password']

    r=Db()
    qry="SELECT * FROM login WHERE username= '"+username+"' AND password = '"+password+"'"
    res= r.selectOne(qry)
    if res != '':
        type=res['usertype']
        if type == "admin":
            return render_template("admin/home.html")
        elif type == "shop":

            session['shop_id'] = res['loginid']
            return render_template("shop/home.html")
    else:
        return 'invalid username or password'






@app.route('/adm_view_order')
def adm_view_order():
    d = Db()

    qry = ("select ordermain.*,customer.name AS cname from ordermain,customer where customer.loginid= ordermain.userid")
    res = d.select(qry)
    return render_template("admin/view_order.html",val=res)

@app.route('/adm_view_items/<id>')
def adm_view_item(id):
    d= Db()
    qry=("select ordersub.*,products.*,shop.name as shop_name from ordersub,products,shop where ordersub.ordermainid='"+id+"' and ordersub.shopid=shop.loginid AND products.prdid=ordersub.productid")
    res=d.select(qry)
    return render_template("admin/view_item.html",val=res)

@app.route('/shop')
def shop():
    return render_template("shop/home.html")

@app.route('/shop_register')
def adm_shop_register():
    return render_template("shop/register.html")

@app.route('/shop_register_post',methods=['post'])
def shop_register_post():
    name= request.form['name']
    address= request.form['address']
    email = request.form['email']
    contact = request.form['contact']
    d= Db()
    qry1 = "insert into login(username,password,usertype)values('" + email + "','" + contact + "','pending')"
    res1 = d.insert(qry1)

    qry = "insert into shop(name,address,email,contact,loginid)values('" + name + "','" + address + "','" + email + "','" + contact + "','" + str(
        res1) + "')"
    res = d.insert(qry)
    return shop()

@app.route('/shop_change_password')
def adm_shop_password():
    return render_template("shop/change_password.html")

@app.route('/shop_change_pass_post',methods=['post'])
def shop_change_pass_post():
    d=Db()
    cur_pass=request.form['cur_pass']
    new_pass = request.form['new_pass']
    confirm_pass = request.form['confirm_pass']
    qry="select password from login where loginid='"+str(session['shop_id'])+"'"
    res=d.selectOne(qry)
    if str(res['password']) == cur_pass:
        if new_pass == confirm_pass:
            qry2="update login set password='"+new_pass+"' where loginid='"+str(session['shop_id'])+"'"
            res2=d.insert(qry2)
        else:
            return ("password not match")
    else:
        return ("please enter correct password")
    return render_template("shop/home.html")

@app.route('/shop_add_category')
def shop_add_category():
    return render_template("shop/add_category.html")

@app.route('/shop_add_category_post',methods=['post'])
def shop_add_category_post():
    category= request.form['category']
    d=Db()
    qry= "insert into category(category)values('"+category+"')"
    res= d.insert(qry)
    return shop_add_category()

@app.route('/shop_add_product')
def shop_add_product():
    d=Db()
    qry= "select * from category"
    res=d.select(qry)
    return render_template("shop/add_product.html",val=res)


@app.route('/shop_add_product_post',methods=['post'])
def shop_add_product_post():
    name = request.form['name']
    description = request.form['description']
    category= request.form['category']
    made_date = request.form['made_date']
    exp_date = request.form['exp_date']
    price = request.form['price']
    pic = request.files['img']
    pic.save("C:\\Users\\THIS PC\\PycharmProjects\\evengara\\static\\imgs\\products\\" + pic.filename)
    path = "/static/imgs/products/" + pic.filename
    d=Db()
    qry= "insert into products(name,image,description,madedate,expdate,price,categoryid,shopid)values('"+name+"','"+path+"','"+description+"','"+made_date+"','"+exp_date+"','"+price+"','"+category+"','"+str(session['shop_id']) +"')"
    res= d.insert(qry)
    return shop_add_product()

@app.route('/shop_view_products')
def shop_view_products():
    r = Db()
    
    qry = "select products.*,category.category from products,category where products.shopid='"+str(session['shop_id'])+"' and products.categoryid=category.cat_id"
    res = r.select(qry)
    return render_template("shop/view_products.html",val=res)


@app.route('/shop_edit_products/<id>')
def shop_edit_products(id):
    r = Db()

    qry = "select * from products where prdid = '"+id+"'"
    res = r.selectOne(qry)
    qry2="select * from category"
    res2=r.select(qry2)
    return render_template("shop/edit_product.html", val=res, val2=res2)

@app.route('/shop_edit_product_post',methods=['post'])
def shop_edit_product_post():
    id=request.form['id']
    name = request.form['name']
    description = request.form['description']
    category= request.form['category']
    made_date = request.form['made_date']
    exp_date = request.form['exp_date']
    price = request.form['price']
    d = Db()
    if "img" in request.files:

        pic =request.files['img']
        if pic.filename != "" :
            pic.save("C:\\Users\\THIS PC\\PycharmProjects\\evengara\\static\\imgs\\products\\" + pic.filename)
            path = "/static/imgs/products/" + pic.filename
            qry="UPDATE products SET name ='"+name+"',image ='"+path+"',description ='"+description+"',madedate ='"+made_date+"',expdate='"+exp_date+"',price='"+price+"',categoryid='"+category+"' where prdid='"+id+"'"
            res = d.update(qry)
        else :
            qry = "UPDATE products SET name ='"+name+"',description ='"+description+"',madedate ='"+made_date+"',expdate='"+exp_date+"',price='"+price+"',categoryid='"+category+"' where prdid='"+id+"'"
            res = d.update(qry)
    else :
        qry = "UPDATE products SET name ='"+name+"',description ='"+description+"',madedate ='"+made_date+"',expdate='"+exp_date+"',price='"+price+"',categoryid='"+category+"' where prdid='"+id+"'"
        res = d.update(qry)


    return shop_view_products()


@app.route('/shop_delete_products/<id>')
def adm_delete_products(id):
    r = Db()
    qry="delete from products where prdid='"+id+"'"
    res = r.delete(qry)
    return shop_view_products()
    
@app.route('/shop_search_product',methods=['post'])
def shop_search_productr():
    d = Db()
    search = request.form['search']
    qry= "SELECT products.*,category.category FROM products,category WHERE products.name LIKE '%"+search+"%' and  products.shopid='"+str(session['shop_id'])+"' and  products.categoryid=category.cat_id"
    res=d.select(qry)
    return render_template("shop/view_products.html",val=res)


@app.route('/shop_add_notification')
def shop_add_notification():
    return render_template("shop/addnotification.html")


@app.route('/shop_add_notification_post',methods=['post'])
def shop_add_notification_post():
    notification=request.form['textarea']
    c=Db()
    qry="insert into notification(notification,date)values('"+notification+"',curdate())"
    rr=c.insert(qry)
    return shop_add_notification()

@app.route('/shop_view_notification')
def shop_view_notification():
    c=Db()
    qry="select * from notification"
    tt=c.select(qry)
    return render_template("shop/viewnotification.html",data=tt)

@app.route('/shop_view_profile')
def shop_view_profile():
    c=Db()

    qry="select * from shop where loginid= '"+str(session['shop_id'])+"'"
    tt=c.select(qry)
    return render_template("shop/view_profile.html",data=tt)

@app.route('/shop_view_reviews')
def shop_view_reviews():
    r = Db();
    qr="select shopid from shop where loginid='"+str(session['shop_id'])+"'"
    re=r.selectOne(qr)

    qry = "SELECT review.*,customer.name AS cname FROM review,customer WHERE customer.loginid = review.userid AND review.id='"+str(re['shopid'])+"' AND review.type='shop'"
    res = r.select(qry)
    return render_template("shop/view_review.html",val=res)

@app.route('/shop_add_offer')
def shop_add_offer():
    d = Db()
    qry = "select * from products WHERE shopid='"+str(session['shop_id'])+"'"
    res = d.select(qry)
    return render_template("shop/offer.html", val=res)

@app.route('/shop_add_offer_post',methods=['post'])
def shop_add_offer_post():
    name = request.form['name']
    description = request.form['description']
    product= request.form['product']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    d = Db()
    qry = "insert into offer(offername,description,startdate,enddate,productid,shopid)values('" + name + "','" + description + "','" + start_date + "','" + end_date + "','" + product + "','" + str(
        session['shop_id']) + "')"
    res = d.insert(qry)
    return shop_add_offer()

@app.route('/shop_view_offer')
def shop_view_offer():
    d = Db()
    qry = "select products.name AS product,offer.* from products,offer WHERE offer.shopid = '"+str(session['shop_id'])+"' and products.prdid = offer.productid"
    res = d.select(qry)
    return render_template("shop/view_offer.html", val=res)


@app.route('/shop_delete_offer/<id>')
def adm_delete_offer(id):
    r = Db()
    qry = "delete from offer where offerid='" + id + "'"
    res = r.delete(qry)
    return shop_view_offer()

@app.route('/shop_view_order')
def shop_view_order():
    d = Db()
    shop=session['shop_id']
    qry=("select distinct ordermain.*,ordersub.shopid,customer.name AS cname from ordermain,ordersub,customer where customer.loginid= ordermain.userid AND ordermain.ordermainid = ordersub.ordermainid and ordersub.shopid = '"+str(shop)+"'")
    res=d.select(qry)

    return render_template("shop/view_order.html", val=res)

@app.route('/shop_view_item/<id>')
def shop_view_item(id):
    d = Db()
    qry="select ordersub.*,products.* from ordersub,products where ordersub.ordermainid='"+id+"' and ordersub.shopid ='"+str(session['shop_id'])+"' AND products.prdid=ordersub.productid"
    res=d.select(qry)
    return render_template("shop/view_item.html",val=res)
@app.route("/chat")
def chat():
    return render_template("shop/chat.html")


@app.route("/emp_chat_chk",methods=['post'])        # refresh messages chatlist
def emp_chat_chk():

    qry = "SELECT DATE,message,senderid FROM chat WHERE (senderid='" + str(
        session['shop_id']) + "' AND reciverid=1) OR ((senderid=1 AND reciverid='" + str(
        session['shop_id']) + "')) ORDER BY chatid DESC"
    c = Db()
    res = c.select(qry)
    return jsonify(res)


@app.route("/emp_chat_post",methods=['POST'])
def emp_chat_post():
    id=1
    ta=request.form["ta"]
    qry="insert into chat(message,date,time,senderid,reciverid,type) values('"+ta+"',CURDATE(),CURTIME(),'"+str(session['shop_id'])+"','"+str(id)+"','shop')"
    d=Db()
    d.insert(qry)
    return render_template('shop/chat.html')

if __name__ == '__main__':
    app.run(debug=True)