/**
 * Created by gamer on 13.04.2018.
 */


   var btn = document.getElementsByName("submit");


    btn[0].onclick = function (e) {
        e.preventDefault();

        var cartItem = document.querySelectorAll(".cart-item");
        var data = {"name" : '', "email" : '', "telephone" : '', "address" : '', "msg" : '', "bluda" : '', "price": '', 'csrfmiddlewaretoken': ['Kv1y1U54OUNkHW1q7MJcsxZpcSArAPIQyXyxdkhkfibW6zObKv7obGUmkuyOoiJE']};
        var name = document.getElementById("name");
        var email = document.getElementById("contact-email");
        var mobile = document.getElementById("mobile");
        var address = document.getElementById("subject");
        var msg = document.getElementById("message");



        data.name += name.value;
        data.email += email.value;
        data.telephone += mobile.value;
        data.address += address.value;
        data.msg += msg.value;


        for(var i=0; i < cartItem.length; i++) {
            for(var j=0; j < cartItem[i].childNodes.length; j++) {
                if(j === 1) {
                    data.bluda += cartItem[i].children[j].innerText + ",";
                }
                else if(j === 2) {
                    data.price += cartItem[i].children[j].innerText + ",";
                }
            }
        }


           function post(path, params, method) {
            method = method || "post"; // Set method to post by default if not specified.

            // The rest of this code assumes you are not using a library.
            // It can be made less wordy if you use one.
            var form = document.createElement("form");
            form.setAttribute("method", method);
            form.setAttribute("action", path);

            for (var key in params) {
                if (params.hasOwnProperty(key)) {
                    var hiddenField = document.createElement("input");
                    hiddenField.setAttribute("type", "hidden");
                    hiddenField.setAttribute("name", key);
                    hiddenField.setAttribute("value", params[key]);

                    form.appendChild(hiddenField);
                }
            }

            document.body.appendChild(form);
            form.submit();
        }
        post('zakaz/', data)
    };

