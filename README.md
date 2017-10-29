# grim_banshee
A GUI to train mouse and keyboard sequences.

Overview:
Grim Banshee automates a sequence of mouse and/or keyboard commands. It stores the sequences in 10 possible memory locations that you can toggle during training.  After or during training, if you click Do, Do All, or Repeat, the tasks trained so far will be automatically performed for you.  Your progress is automatically saved after every training.
 
Advanced:
When the Do button is clicked, only the tasks in memory #X are done.  For the Do case, those tasks will be done 1 time.  For a repeated Do case (when reps is greater than 0), those tasks will be repeated  any number of times as set in the reps box.  The Do All button has more options.  The default case is when the random and rigid checkboxes are unchecked.  In the default case, tasks will be preformed starting in memory #1 until complete, and then tasks in memory #2 will be done, and so on.  Also, a text comparison conditionality can be configured to determine whether to proceed to the next memory.  If 'always' is selected, there is no condition; it always advances.  If 'same' is selected, then it advances only if the text in the two text boxes (top and bottom) are the same.  If 'diff' is selected, then it advances only if the text in the two text boxes are different.  If you click Do All when 'random' is check-marked, then the memories will be invoked in random memory order:  example:  2 could come before 1.  But all tasks within the memory are executed in order.  If a Do All 'rigid' case is done, then the tasks will be done in order of the saved settings in either your GB_save.txt file or your custom named file (in either case you have to Load or Load As them first).  That means all tasks will have a memory #1.  To accomplish this when training, you can use a tilda (~) command to switch memories.  Then do a tisk ` command to exit the second memory to return to training the first memory.  Do All can be repeated as similar to Do by increasing the number in the reps box.

Example basic process flow:
Step 1. After you click Train, click on the terminal and enter a command.
Step 2. If applicable, move the mouse to a screen location where the command is to be done.  Hint:  You can use Alt-Tab to focus back to the terminal.
Step 3. Press the Enter key (focus must be on terminal).
Step 4. That completes one command in the training sequence.
Step 5+ Repeat as you like; make sure new commands are typed into the terminal.
Step next to last.  Press the ` key and Enter to stop training.
Step last. Now click the Do button to run your command sequence.

Buttons:
Clear = clear memory for training in memory #X.  Otherwise, new commands will be appended to end of existing training.
Clearall = clear all training memory and liberate all keyboard and mouse buttons
Train = store a sequence of key commands in memory #X
Do = execute sequence of key commands in memory #X
Do All = execute all memory sequences in order
Rand = apply random ordering to Do All process
Rigid = when Load or Load As is clicked, the next Do All will perform the tasks in the order indicated in the loaded file as if all memories are 1.
#X = which memory to clear, train, or do.  Use menu (e.g. 1).
Save and Save As = saves a text file with all training.  Avoid using | in your 't' commands because that is delimiter. Progress is automatically saved to GB_Save.txt.
Load and Load As = loads a text file with training settings.

For Do All, use top and bottom text boxes for text comparison as follows:
Always = always execute the next Training (e.g. 2 after 1.)
Diff = only execute the next training if two text boxes are different
Same = only execute the next training if two text boxes are same

Key mappings for 'k', 'kd', 'ku', and 'hk' commands:
enter,  esc,  \n,  shift,  alt,  ctrl,  tab,  backspace,  delete,  pageup,  pagedown,  home,  end,  up,  down,  left,  right,  f1,  f2,  f3,  f4,  f5,  f6,  f7,  f8,  f9,  f10,  f11,  f12,  command,  volumemute,  volumedown,  volumeup,  pause,  capslock,  numlock,  scrolllock,  insert,  printscreen,  winleft,  winright,  

Rigid Training:
Utilize ~ and ` during training to toggle between memories as follows.
Step 1. Select a memory location by toggling the memory menu box (call this first).
Step 2. After you click Train, click on the terminal.
Step 2+ Enter commands into the first memory as you like.
Step 3. Select a new memory location with the training memory menu (call this second).
Step 4. Click on the terminal to bring it to focus.
Step 5. Type a ~ command and press Enter.  You may now enter commands to the second memory.
Step 6. When you are finished adding training commands to the second memory location, enter a ` command and press enter.
Step 7. This returns you to the first training, where you can continue training or exit with another ` command.
Tip:  During any training which requires that you wait for another application to process, you may want to use the ` command to exit out of training before starting that application.  This avoids Grim Banshee crashing.  In general, use ` or ~ before toggling new memory rings or time box.

Command mapping:
L or l = left click
R or r = right click
D or d = double left click
b = delete previous command
h = hold left mouse button and drag mouse to position, then copy to OS clipboard.
c = highlight, copy, and save in top text box
v = paste from top text box to mouse position
cc = highlight, copy, and save in bottom text box
vv = paste from bottom text box to mouse position
su = scroll up
sd = scroll down
lhd = left click and hold down
lhu = left unclick
rhd = right click and hold down
rhu = right unclick
t = type in text (enter on next prompt)
k = press any single keyboard key
kd = press and hold single key
ku = lift up single key
hk = hotkey combination
` = done training in memory #X
~ = start a new training mode without needing to finish old one.  Change memory before pressing Enter.
Enter button = associate mouse position with key command preceding.
help = mini-help (just commands)


