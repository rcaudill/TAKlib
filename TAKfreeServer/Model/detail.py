#######################################################
#
# detail.py
# Python implementation of the Class detail
# Generated by Enterprise Architect
# Created on: 11-Feb-2020 11:08:07 AM
# Original author: Corvo
#
#######################################################


class Detail:
    """An optional element used to hold CoT sub-schema. empty element
    """
    def __init__(self,linkType=None , uid = None,linkuid=None ,linkproduction_time=None, linkrelation=None, linktype=None, linkparent_callsign=None, connType = None, chatType = None, chatsenderCallsign = None, chatchatroom = None, chatgroupOwner = None, chatid = None, chatparent = None, chatgrpuid0 = None, chatgrpuid1 = None, arg10 = None, arg11 = None):
        argumentsRecieved = locals()

        args = self.createArguments(argumentsRecieved)

        case = {
            'chat': self.chatFunc,
            'ping': self.pingFunc,
            'timeout':self.timeoutFunc
            }

        case[connType](args)

    def createArguments(self, argumentsRecieved):
        argumentsToBePassed = {}
        for x, y in argumentsRecieved.items():
            if x != 'self' and x != 'argumentsRecieved' and y != None:
                argumentsToBePassed[x] = y
            else:
                pass
        return argumentsToBePassed
    
    def pingFunc(self,info):
        pass

    def chatFunc(self, info):
        from Model.chat import chat
        chat = chat(chatType = info['chatType'], senderCallsign = info['senderCallsign'] , chatroom = info['chatroom'], groupOwner = info['groupOwner'], id = info['id'], parent = info['parent'], uid0 = info['uid0'], uid1 = info['uid1'])
        self.chat = chat
    
    def timeoutFunc(self, info):
        from Model.link import link
        self.link = link(linkType = info['linkType'],linktype = info['linktype'] ,linkuid=info['linkuid'],linkrelation = info['linkrelation'])