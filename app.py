from flask import Flask,render_template,Response
app=Flask(__name__)
import warnings
warnings.filterwarnings("ignore")
from sqlalchemy import create_engine
import pandas as pd
import psycopg2 


@app.route('/')
def index():
    return render_template('index.html')    


@app.route('/table',methods=['GET','POST'])
def table():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres")
    jobs_df = pd.read_sql("SELECT * FROM job_listings",engine)
    print(jobs_df)
    html_table = jobs_df.to_html(
    index=False,
    classes="table table-striped table-hover table-bordered"
    )
    return render_template('table.html',html_table=html_table)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=False, port= 5000)
