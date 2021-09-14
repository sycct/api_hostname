#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from ipaddress import ip_address

import requests
from flask import Flask, jsonify
from requests import exceptions

app = Flask(__name__)


@app.route('/hostname/<string:ip>')
def get_hostname(ip):
    reverse_name = ip_address(ip).reverse_pointer
    uri = f"https://dns.google/resolve?name={reverse_name}&type=PTR"
    try:
        get_result = requests.get(uri, timeout=1)
    except (exceptions.ConnectionError, exceptions.HTTPError, exceptions.Timeout) as e:
        message = {'success': False, 'message': e}
        return jsonify(message)
    result_json = get_result.json()
    try:
        get_answer = result_json['Answer'][0]
    except KeyError:
        return jsonify({'success': False, 'message': '解析出现错误！'})
    get_type = get_answer['type']
    if get_type == 12:
        # 转换成域名形式
        host = get_answer['data'][0:-1]
        return jsonify({'success': True, 'hostname': host})
    else:
        return jsonify({'success': False, 'message': '无结果'})


if __name__ == '__main__':
    app.run()
