from flask import Flask, abort, request, jsonify

from index import getDescByLink


app = Flask(__name__)

# 测试数据暂时存放
tasks = []

@app.route('/get_url', methods=['GET'])
def get_task():
  url = request.args['url']
  print(url)
  dataBase = getDescByLink(url)
  return dataBase
    # if not request.args or 'id' not in request.args:
    #     # 没有指定id则返回全部
    #     return jsonify(tasks)
    # else:
    #     task_id = request.args['id']
    #     task = filter(lambda t: t['id'] == int(task_id), tasks)


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)
