#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request
import jieba

app = Flask(__name__)

tags = [
    u'自己',
    u'系統',
    u'相處',
    u'溝通',
    u'曖昧',
    u'擇偶',
    u'性愛',
    u'安全感',
    u'婚姻',
    u'多重關係',
    u'刪除題意不清',
    u'分手',
    u'其他'
]

@app.route('/reply/tags', methods=['POST'])
def get_tags():
    if not request.json or not 'sentence' in request.json:
        abort(400)

    sentence = request.json['sentence']
    get_tags = []

    words = jieba.cut(sentence, cut_all=False)
    for word in words:
        try:
            get_tags = tags[tags.index(word)]
        except:
            pass

    return jsonify({'tags': get_tags})

if __name__ == '__main__':
    app.run(debug=True)