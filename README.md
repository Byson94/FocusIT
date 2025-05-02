# FocusIT

Focusit is a simple program to keep track of the time you spend on a task.

> NOTE: This program can be used only on unix based systems. If you use windows, the code will not work on your system.

## Download the program:

Run the following command to clone the repository to your system (you can install repository as .zip if you want to)

```bash
git clone https://github.com/Byson94/FocusIT
```

## Prerequisites

Make sure that you have the prerequisites to run the program or else it will not work.

- **Prerequisites**
  - **rich**

**Run the following command to install the prerequisites.**

```bash
pip install -r requirements.txt
```

## Notes

- If you are running this program locally, then make sure to run `python -m venv ./venv` to setup a virtual enviornment to install the prerequisites to.

- If you want to run this program globally, then running the following command will make it globally accessable by calling `focusit` (make sure that the prerequisites are installed to your system to make it run)

```bash
sudo cp main.py /usr/local/bin/focusit
```

After running that, run the following code so that you can call it without any permission issues.

```bash
chmod +x /usr/local/bin/focusit
```

- The above commands copies the python script and gives it permission to execute aswell as making it trigger when focusit is triggered.
