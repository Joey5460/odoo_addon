update:
	./odoo/odoo-bin -d todo -u todo_app
run:
	./odoo/odoo-bin -d todo --addons-path="custom-addons,odoo/addons" -u todo_app --dev=all
test:
	./odoo/odoo-bin -d todo --addons-path="custom-addons,odoo/addons" -i todo_app --test-enable 

init:
	./odoo/odoo-bin
