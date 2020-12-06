Документация Python: https://www.python.org/

# Generte ssh-key for git
 * ssh-keygen -t rsa -b 4096 -C "your.email@mail.com"
 * add public-key into github account

# Ubuntu sublime-text installation steps:
* Install the GPG key:
  - wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

* Ensure apt is set up to work with https sources:
  - sudo apt-get install apt-transport-https

* Select the channel to use:
  - echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list 
  - echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

* Update apt sources and install Sublime Text 
  - sudo apt-get update
  - sudo apt-get install sublime-text
  

# Examples requirements
### Generate output suitable for a requirements file.
  - $ python -m pip freeze
      - docutils==0.11
      - Jinja2==2.7.2
      - MarkupSafe==0.19
      - Pygments==1.6
      - Sphinx==1.2.2
  
### Generate a requirements file and then install from it in another environment.
  - Unix/macOS
    - python -m pip freeze > requirements.txt
    - python -m pip install -r requirements.txt