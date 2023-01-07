To run this application you need python3 with module in the requirements.txt file installed.
Run 'pip install requirements' or manually 'pip install pvrecorder' and 'pip install pvrhino'.



Now you can do the following steps.


1 - Login to Picovoice.

2 - Go to Picovoice console and get your KEY.

3 - From Picovoice consolo go to Rhino Speech-to-intent.

4 - Create new context (use minimum two words commands).

5 - Download context file (.rnh)

6 - If you need other language download it from https://github.com/Picovoice/rhino/tree/master/lib/common

7 - Replace path in mac_command.py

8 - Replace path in mac_command_launcher.plist

9 - Save mac_command_launcher.plist in /Library/LaunchAgents/mac_command_launcher.plist




You can run script at startup:


to activate run: launchctl load /Library/LaunchAgents/mac_command_launcher.plist

to deactivate run: launchctl unload /Library/LaunchAgents/mac_command_launcher.plist



You can create as many commands as you like. Enjoy.
https://chris-maker.com/


Iannella Christian 07/01/2023