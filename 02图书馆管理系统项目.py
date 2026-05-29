# # encoding=utf-8
# '''
# 1,图书管理系统的界面设置
#     用户输入不同的数字 执行不同的功能
# 2,我们创建一个书籍表 book  字段 id 主键 自增  书名 作者 简洁
# 3.用户可以自由插入数据
# 4，用户可以查询全部数据
# 5，用户可以根据id 查询指定数据
# 6，用户可以根据id 修改指定该数据
# 7，用户可以根据id  删除指定数据
# 8，退出
# '''
import pymysql
from IPython.core.release import author


# 修正逻辑
def get_input_ini(def_value):
    user_input = input(f'默认值为：{def_value}，直接回车使用默认值，否则请输入新内容：')
    return def_value if user_input.strip() == '' else user_input


# ==============数据模型类===========
class Books:
    def __init__(self, id, name, author, dsc):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__dsc = dsc

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_dsc(self):
        return self.__dsc

    def set_name(self):
        self.__name = get_input_ini(self.__name)
        return self.__name

    def set_author(self):
        self.__author = get_input_ini(self.__author)
        return self.__author

    def set_dsc(self):
        self.__dsc = get_input_ini(self.__dsc)
        return self.__dsc


# ===========数据库操作类=============
class Mysql_book:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='123456',
            db='pymysql_test',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def add_book(self, args):
        try:
            sql = ('insert into book values(%s,%s,%s,%s)')
            self.cursor.execute(sql, args)
            self.conn.commit()
            print('插入成功！')
        except Exception as e:
            print('插入失败：', e)
        finally:
            self.cursor.close()
            self.conn.close()

    def select_all_book(self):
        try:
            sql = 'select * from book'
            self.cursor.execute(sql)
            print('查询成功！')
            row = self.cursor.fetchall()
            for rn in row:
                print(rn)
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('查询失败：', e)
            self.cursor.close()
            self.conn.close()

    def select_one_book(self, id_1):
        try:
            sql = 'select * from book where id = %s'
            self.cursor.execute(sql, id_1)
            row = self.cursor.fetchone()
            if row is None:
                print('没有该数据！')
            else:
                print(f'查询成功！id={id_1}的数据为：')
                print(row)
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(f'查询失败，未搜索到id={id_1}的数据！失败原因为：', e)
            self.cursor.close()
            self.conn.close()

    def update_book(self, id_1):
        try:
            sql = 'select * from book where id = %s'
            self.cursor.execute(sql, id_1)
            row = self.cursor.fetchone()
            print(f'查询成功，你要修改的数据内容：{row}')
            book = Books(row[0], row[1], row[2], row[3])
            name = book.set_name()
            author = book.set_author()
            dsc = book.set_dsc()
            sql = 'update book set bname = %s,writer = %s,tag = %s where id = %s'
            args = (name, author, dsc, id_1)
            self.cursor.execute(sql, args)
            self.conn.commit()
            print('修改成功！')
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('修改失败：', e)
            self.cursor.close()
            self.conn.close()

    def delete_book(self, id_1):
        try:

            sql = 'delete from book where id = %s'
            self.cursor.execute(sql, id_1)
            self.conn.commit()
            print('删除成功！')
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('删除失败：', e)


# ================主程序===============
if __name__ == '__main__':
    while 1:
        # 显示菜单
        print('-' * 30, '欢迎进入图书管理系统', '-' * 30)
        print("'1':'插入数据'")
        print("'2':'查询全部数据'")
        print("'3':'查询一条数据'")
        print("'4':'修改数据'")
        print("'5':'删除数据'")
        print("'6':'退出'")
        # ++++++++++++++++功能选择+++++++++++++++++
        user_select = input("请输入你的选择(1-6):")

        # 1.插入一条数据
        if user_select == '1':
            name = input('请输入书的名字：')
            author = input('请输入作者的名字：')
            dsc = input('请输入简介：')
            # 将采集到的数据封装成对象保存到book
            book = Books(None, name, author, dsc)
            # 创建数据库操作对象mysql_book
            mysql_book = Mysql_book()
            # 调用添加方法，传入插入图书信息元组
            mysql_book.add_book((
                None,
                book.get_name(),
                book.get_author(),
                book.get_dsc()
            ))

        # 2.查询全部数据
        elif user_select == '2':
            mysql_book = Mysql_book()
            mysql_book.select_all_book()

        # 3.查询一条数据
        elif user_select == '3':
            mysql_book = Mysql_book()
            id_1 = input('请输入id：')
            mysql_book.select_one_book(id_1)

        # 4.修改一条数据
        elif user_select == '4':
            id_1 = input('请输入要修改的数据id：')
            mysql_book = Mysql_book()
            mysql_book.update_book(id_1)
            print('正在为您查询修改后数据......')
            Mysql_book().select_one_book(id_1)


        # 5.删除一条数据
        elif user_select == '5':
            try:
                id_1 = input('请输入要删除的数据id：')
                print('您将删除如下数据：')
                Mysql_book().select_one_book(id_1)
                print('请再次确认是否删除该数据(y/n)：')
                confirm = input()
                if confirm == 'y':
                    mysql_book = Mysql_book()
                    mysql_book.delete_book(id_1)
                    print('正在为您查询删除后的所有数据......')
                    Mysql_book().select_all_book()
                elif confirm == 'n':
                    print('已取消删除！')
                else:
                    print('请输入正确的指令！')
            except Exception as e:
                print('删除失败,遇到了错误：', e)


        # 6.退出
        elif user_select == '6':
            break;
            print('退出成功！')
        else:
            print('请正确输入(1-6)')
