from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

contact_app = Blueprint("contact", __name__)


Teams = {
    0: 'Morning',
    1: 'Daytime',
    2: 'Evening',
}


@contact_app.route("/", methods=["GET","POST"])
def contact_form():
    time = int(request.form.get('time', 0))
    return render_template("contact.html", time=time, team=Teams[time])

#
# @contact_app.route("/<int:product_id>/", methods=['GET', 'DELETE'])
# def product_detail(product_id: int):
#     try:
#         product_name = PRODUCTS[product_id]
#     except KeyError:
#         raise BadRequest(f"Invalid product id #{product_id}")
#
#     if request.method == 'DELETE':
#         PRODUCTS.pop(product_id)
#         return jsonify(ok=True)
#
#     return render_template(
#         "products/detail.html",
#         product_id=product_id,
#         product_name=product_name,
#     )