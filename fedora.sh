sudo dnf install $(cat dnflist)
sudo postgresql-setup --initdb --unit postgresql
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo su - postgres -c "createuser -s $USER"
sudo npm install -g less
