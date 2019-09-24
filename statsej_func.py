# -*- coding: utf-8 -*-
import sqlite3
def search_result(jaen, form_input): # ()
    """
    日本語→英語: 0, 英語→日本語: 1
    """
    conn = sqlite3.connect('statisticsEJ.db')
    c = conn.cursor()
    # form_input = "1discrete data" # テスト用
    # jaen = '1'
    form_input = form_input[1:]
    if jaen == '0':
        result_l = c.execute('SELECT en FROM statisticsEJ WHERE ja=:form_input', {'form_input': form_input})
    else:
        result_l = c.execute('SELECT ja FROM statisticsEJ WHERE en=:form_input', {'form_input': form_input})
    result_l = result_l.fetchone()
    return result_l[0]
