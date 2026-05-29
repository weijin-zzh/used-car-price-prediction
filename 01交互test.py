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
    # 包含编号id ,姓名name ,性别gender ,年龄age
    # sql = """
    #     create table student1(
    #         id int auto_increment primary key,
    #         name varchar(20) not null ,
    #         gender varchar(8) not null,
    #         age int not null
    #
    #     )
    #
    # """

    # 添加数据
    # try:
    #
    #     name = input('请输入你的姓名:')
    #     gender = input('请输入你的性别:')
    #     age = input('请输入你的年龄:')
    #     params = (name,gender,age)
    #     sql = '''
    #     insert into student1 (name,gender,age)values (%s,%s,%s)
    #     '''
    #     cursor.execute(sql,params)
    #     db_conn.commit()
    #     print('添加成功!!!')
    #     cursor.close()
    #     db_conn.close()
    # except Exception as e:
    #     print('添加失败:',e)
    #     cursor.close()
    #     db_conn.close()

    # 修改数据
    # try:
    #     sql = '''
    #     update student1 set name = '小明' where id = 2               '''
    #     cursor.execute(sql)
    #     db_conn.commit()
    #     print('修改成功!!!')
    #     cursor.close()
    #     db_conn.close()
    # except Exception as e:
    #     print('修改失败:', e)
    #     cursor.close()
    #     db_conn.close()

    # 删除数据
    # try:
    #     sql = '''
    #     delete from student where id = 2               '''
    #     cursor.execute(sql)
    #     db_conn.commit()
    #     print('删除成功!!!')
    #     cursor.close()
    #     db_conn.close()
    # except Exception as e:
    #     print('删除失败:', e)
    #     cursor.close()
    #     db_conn.close()

    # 查询数据
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

