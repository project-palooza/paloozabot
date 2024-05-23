from utils.listify_logs import listify_log
from utils.jsonify_log import jsonify_log


with open('paloozabot.log','r') as file:
    log_data = file.read()

log_list = listify_log(log_data)