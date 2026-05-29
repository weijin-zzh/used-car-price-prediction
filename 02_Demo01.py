import pymysql
from pymysql import cursors

if  __name__ ==  "__main__":
    db_conn = pymysql.connect(
        user= 'root',
        password='123456',
        host='localhost',
        port=3306,
        db='ecommerce_analysis1',
        charset='utf8',
        cursorclass=cursors.DictCursor
    )
    cursor = db_conn.cursor()

    try:
        sql = '''
        SELECT
    COUNT(DISTINCT user_id) AS 新增用户数  -- 去重统计唯一用户ID数量
FROM
    user_master  -- 用户主表
WHERE
    register_time BETWEEN
        DATE_SUB(CURDATE(), INTERVAL 30 DAY)  -- 起始日期：当前日期往前推30天（含当天）
        AND
        CURDATE();  -- 结束日期：当前日期（含当天）
              '''
        cursor.execute(sql)
        db_conn.commit()
        # 查询一行
        # f = cursor.fetchone()
        f = cursor.fetchall()
        for row in f:
            print(row)
        print('查询成功!!!')
        cursor.close()
        db_conn.close()
    except Exception as e:
        print('查询失败:', e)
        cursor.close()
        db_conn.close()

# import pandas as pd
# import mysql.connector
#
# # 1. 连接数据库
# conn = mysql.connector.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='your_password',
#     database='ecommerce_db',
#     charset='utf8mb4'
# )
#
# # 2. 执行查询获取数据
# sql = """
# SELECT
#     o.order_id,
#     u.username,
#     o.order_time,
#     o.total_amount,
#     o.payment_amount,
#     o.payment_status
# FROM order_master o
# JOIN user_master u ON o.user_id = u.user_id
# WHERE o.order_time >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
# """
#
# df = pd.read_sql(sql, conn)
# conn.close()
#
# # 3. 数据处理（可选）
# # 例如：格式化时间、计算衍生字段等
# df['order_time'] = pd.to_datetime(df['order_time']).dt.strftime('%Y-%m-%d %H:%M:%S')
# df['discount_amount'] = df['total_amount'] - df['payment_amount']
#
# # 4. 导出为 CSV
# df.to_csv('order_export.csv', index=False, encoding='utf-8-sig')
# print(f"成功导出 {len(df)} 条数据到 order_export.csv")
