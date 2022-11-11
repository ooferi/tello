import djitellopy
from djitellopy import Tello
import time

def connect(self, wait_for_state=True):
    """Enter SDK mode. Call this before any of the control functions.
    """
    self.send_control_command("command")

    if wait_for_state:
        REPS = 20
        for i in range(REPS):
            if self.get_current_state():
                t = i / REPS  # in seconds
                Tello.LOGGER.debug("'.connect()' received first state packet after {} seconds".format(t))
                break
            time.sleep(1 / REPS)

        if not self.get_current_state():
            raise Exception('Did not receive a state packet from the Tello')

def connect_to_wifi(self, ssid, password):
    cmd = 'ap {} {}'.format(ssid, password)
    self.send_command_without_return(cmd)

def takeoff(self):
    self.send_control_command("takeoff", timeout=Tello.TAKEOFF_TIMEOUT)
    self.is_flying = True

def set_speed(self, x: int):
    self.send_control_command("speed {}".format(x))

def end(self):
    if self.is_flying:
        self.land()
    if self.stream_on:
        self.streamoff()
    if self.background_frame_read is not None:
        self.background_frame_read.stop()
    if self.cap is not None:
        self.cap.release()

    host = self.address[0]
    if host in drones:
        del drones[host]

tello = Tello()
tello.connect
tello.connect_to_wifi("Diego's iPhone", "balls123")


tello.takeoff()
tello.set_speed(10)

print("current battery", tello.get_battery())
pog = input("q to land, a to get acceleration (x,y,z in order), h to get height")
def keydown(self, key):
    if key == pygame.K_UP:  # set forward velocity
        self.for_back_velocity = S
    elif key == pygame.K_DOWN:  # set backward velocity
        self.for_back_velocity = -S
    elif key == pygame.K_LEFT:  # set left velocity
        self.left_right_velocity = -S
    elif key == pygame.K_RIGHT:  # set right velocity
        self.left_right_velocity = S
    elif key == pygame.K_w:  # set up velocity
        self.up_down_velocity = S
    elif key == pygame.K_s:  # set down velocity
        self.up_down_velocity = -S
    elif key == pygame.K_a:  # set yaw counter clockwise velocity
        self.yaw_velocity = -S
    elif key == pygame.K_d:  # set yaw clockwise velocity
        self.yaw_velocity = S



#while pog != "q":
 #   print(tello.get_acceleration_x() ,"\n", tello.get_acceleration_y(), "\n", tello.get_acceleration_z())
  #  time.sleep(2)
    


#tello.get_height()

if pog == "q":
    tello.end()

if pog == "h":
    tello.get_height

