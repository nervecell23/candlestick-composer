from app import corr_app 

@corr_app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    corr_app.run()
