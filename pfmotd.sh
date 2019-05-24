#Install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#Install Fortune
brew install fortune

#Configuring .bash_profile and .bashrc
printf "if [ -f ~/.bashrc ]; then\n\t . ~/.bashrc\nfi" >> ~/.bash_profile
printf "fortune | pinkfloydmotd" >> ~/.bashrc

#Hushlogin to remove lastlogin
touch ~/.hushlogin
