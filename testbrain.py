import argparse
import serial
import time 
import math

from pythonosc import dispatcher
from pythonosc import osc_server

#These variables act as a buffer that lets the serial commands to 
#come in at a nice steady pace. 
melcounter = 1
concounter = 1

def write_serial(letter):  
    if SERIAL:  
        arduino.write(letter)
        print(letter) 

#def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
#        print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)


#def concentration_handler(unused_addr, args, concentration):
    #print("Blink: {}".format(blink))
#    global concounter 
#    if concentration >0.7: 
#        concounter = concounter +1

#    if concentration < 0.7:
#        concounter = concounter - 1

#    if concounter <-10:
#        concounter = 0
    
#    if concounter >10:
#        write_serial(b'C')
#        concounter = 0

def mellow_handler(unused_addr, args, mellow):
    #print("Jaw Clench: {}".format(jaw))
    global melcounter
    if mellow >0.7:  
        melcounter = melcounter + 1

    if mellow <0.7:
        melcounter = melcounter - 1

    if melcounter <-10:
        melcounter = 0
  
    if melcounter >10:
        write_serial(b'M')
        melcounter = 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5005,
                        help="The port to listen on")
    parser.add_argument("--serial",
                        default="COM5",
                        help="Arduino serial port")
    args = parser.parse_args()

    if args.serial:
        print ('setting up serial device at %s' % args.serial)
        SERIAL = True
        arduino = serial.Serial(args.serial)
    else: 
        SERIAL = False

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print) 
#    dispatcher.map("/muse/elements/experimental/concentration", concentration_handler, "Concentration")
    dispatcher.map("/muse/elements/experimental/mellow", mellow_handler, "Mellow")
   
#    dispatcher.map("/muse/eeg", eeg_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever() 