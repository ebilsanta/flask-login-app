from app.api import bp

@bp.route('/sign-up', methods=['POST'])
def sign_up():
    pass

@bp.route("/login", methods=['POST'])
def login():
    pass

@bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    pass    

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    pass

@bp.route('/me', methods=['GET'])
def me():
    pass


