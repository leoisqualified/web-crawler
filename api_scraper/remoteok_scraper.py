# Import packages & libraries
import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = 'https://remoteok.com/api'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' \
'(KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;g = 0.5'
}
def get_job_postings():
    res = requests.get(url=BASE_URL, headers = REQUEST_HEADER)
    return res.json()

def save_job_to_xlxs(data):
    wb = Workbook()
    sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i, header in enumerate(headers):
        sheet.write(0, i, header)
    for i, job in enumerate(data[1:]):
        for j, value in enumerate(job.values()):
            sheet.write(i+1, j, value)
    wb.save('remote_jobs.xlsx')


if __name__ == '__main__':
    json = get_job_postings()[1:]
    save_job_to_xlxs(json)