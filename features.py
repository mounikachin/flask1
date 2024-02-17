from flask import Flask

FAI=Flask(__name__)


@FAI.route('/stringresponse')
def stringresponse():
    return 'this is first view of flask'
if __name__=='__main__':
    FAI.run(debug=True)

