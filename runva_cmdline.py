import traceback

from vacore import VACore
import time
import json

# ------------------- main loop ------------------
if __name__ == "__main__":
    cmd_core = VACore()
    cmd_core.init_with_plugins()
    print("Command-line interface for VoiceAssistantCore.")

    # почему бы сразу не отладить какую-то команду?
    time.sleep(0.5) # небольшой таймаут
    cmd = "привет"
    try:
        cmd_core.execute_next(cmd,cmd_core.context)
    except:
        if cmd == "привет":
            print("Ошибка при запуске команды 'привет'. Скорее всего, проблема с TTS.")
        import traceback
        traceback.print_exc()


    #exit(0) # если нужно - закомментируйте и можно будет работать с командной строкой
    _msg="Enter command (user text like 'привет') or 'exit .,q' or '?' доступные команды"
    print(_msg)
    while True:
        cmd = input("> ")
        if cmd == "exit" or cmd=='.' or cmd==',' or cmd=='q':
            break
        elif cmd=="":
            print(_msg)
        elif cmd=="?":
            print(cmd_core)
            _num=0
            _promt={}
            for _a in cmd_core.commands:
                _num=_num+1
                _promt[_num]=_a
                print(_num,_a)
            while True:
                _num = input("Номер > ")
                if _num=='':
                    break
                else:
                    #print(_num)
                    _val=_promt.get(int(_num))
                    #print(_val)
                    _va=_val.split('|')[0]
                    if _va:
                        cmd=_va
                        print(_va)
                        cmd_core.execute_next(cmd,cmd_core.context)
        else:
            cmd_core.execute_next(cmd,cmd_core.context)