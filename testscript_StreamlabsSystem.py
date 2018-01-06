#---------------------------------------
# Import Libraries
#---------------------------------------
import sys
import serial
import time
from collections import deque

#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = "HookScript"
Website = "https://www.twitch.tv/goldenhooker"
Description = "!play 'coordinates x and y' will run machine"
Creator = "GoldenHooker"
Version = "1.0.0.0"

#---------------------------------------
# Set Variables
#---------------------------------------
m_Response = "This is a test message"
m_Command = "!play"
m_Command2 = "!start"
m_CooldownSeconds = 175
m_CommandPermission = "everyone"
m_CommandPermission2 = "caster"
m_CommandInfo = ""
arduino = serial.Serial('COM3', 9600, timeout=.1)

#---------------------------------------
# [Required] Intialize Data (Only called on Load)
#---------------------------------------
def Init():
    return

#---------------------------------------
# [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):
    if data.IsChatMessage():
        if data.GetParam(0).lower() == m_Command2 and not Parent.IsOnCooldown(ScriptName,m_Command) and Parent.HasPermission(data.User,m_CommandPermission2,m_CommandInfo):
            x = "1000z"
            arduino.write(x)
        if data.GetParam(0).lower() == m_Command and Parent.IsOnCooldown(ScriptName,m_Command) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):
            Parent.SendTwitchMessage("Next turn in: " + str(Parent.GetCooldownDuration(ScriptName, m_Command)) + " seconds")
        if data.GetParam(0).lower() == m_Command and not Parent.IsOnCooldown(ScriptName,m_Command) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):
            s = data.Message
            if len(s) == 15 and s[9] == "x" and s[14] == "y":
                Parent.SendTwitchMessage("Playing: " + data.User)
                Parent.SendTwitchMessage(data.User + "'s coordinates are: " + s[5:])
                arduino.write(s[5:])
                r = s[5:9] + "," + s[9:14] + ";"
                time.sleep(25)
                arduino.write(r)
                Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)
            elif len(s) == 17 and s[10] == "x" and s[16] == "y" and s[12] == "1":
                if s[6] == ("3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") or s[13] == "9":
                    Parent.SendTwitchMessage("Invalid Coords")
                elif s[6] == "2" and (s[7] <> 0 or s[8] <> 0 or s[9] <> 0):
                    Parent.SendTwitchMessage("Invalid Coords")
                elif s[13] == "8" and (s[14] <> "0" or s[15] <> "0"):
                    Parent.SendTwitchMessage("Invalid Coords")
                else:
                    Parent.SendTwitchMessage("Playing: " + data.User)
                    Parent.SendTwitchMessage(data.User + "'s coordinates are: " + s[5:])
                    arduino.write(s[5:])
                    r = s[5:10] + "," + s[10:16] + ";"
                    time.sleep(25)
                    arduino.write(r)
                    Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)
            elif len(s) == 16 and s[11] == " " and s[10] == "x" and s[15] == "y":
                if s[6] == ("3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
                    Parent.SendTwitchMessage("Invalid Coords")
                elif s[6] == "2" and (s[7] <> 0 or s[8] <> 0 or s[9] <> 0):
                    Parent.SendTwitchMessage("Invalid Coords")
                else:
                    Parent.SendTwitchMessage("Playing: " + data.User)
                    Parent.SendTwitchMessage(data.User + "'s coordinates are: " + s[5:])
                    arduino.write(s[5:])
                    r = s[5:10] + "," + s[10:15] + ";"
                    time.sleep(25)
                    arduino.write(r)
                    Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)
            elif len(s) == 16 and s[11] == "1" and s[9] == "x" and s[15] == "y":
                if s[12] == "9":
                    Parent.SendTwitchMessage("Invalid Coords")
                elif s[12] == "8" and (s[13] <> 0 or s[14] <> 0):
                    Parent.SendTwitchMessage("Invalid Coords")
                else:
                    Parent.SendTwitchMessage("Playing: " + data.User)
                    Parent.SendTwitchMessage(data.User + "'s coordinates are: " + s[5:])
                    arduino.write(s[5:])
                    r = s[5:9] + "," + s[9:15] + ";"
                    time.sleep(25)
                    arduino.write(r)
                    Parent.AddCooldown(ScriptName, m_Command, m_CooldownSeconds)
            else:
                Parent.SendTwitchMessage("Invalid coords")
    return

#---------------------------------------
# [Required] Tick Function
#---------------------------------------
def Tick():
 return
