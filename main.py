from flask import Flask
from flask import render_template, url_for, abort, redirect, flash
from forms import ClusterSearchForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'KKW5IHaIFWldmvrMi7lGsw'

@app.route("/<cluster>")
def cluster_page(cluster):
    clusterList = ["Bcomm", "Bdsp", "Bmain", "Bvision", "Bimage"]
    if cluster in clusterList:
        return render_template("cluster.html", cluster=cluster)
    else:
        return render_template("error.html")

@app.route("/", methods=['GET', 'POST'])
def home():
    form = ClusterSearchForm()
    if form.validate_on_submit():
        clusterList = ["Bcomm", "Bdsp", "Bmain", "Bvision", "Bimage"]
        clusterName = form.name.data
        if clusterName in clusterList:
            return redirect(url_for('cluster_page', cluster=clusterName))
        else:
            return render_template("error.html")
    return render_template("home.html", form=form)

@app.route("/<cluster>/list")
def rotation_list_page(cluster):
    rotationList = [
        {
            'name': 'Jayadev',
            'email': 'jvasanth@mathworks.com'
        },

        {
            'name': 'Lekshmi',
            'email': 'lprathap@mathworks.com'
        },

        {
            'name': 'Vishnu',
            'email': 'vnair@mathworks.com'
        }
    ]
    return render_template("rotation_list.html", cluster=cluster, rotationList=rotationList)