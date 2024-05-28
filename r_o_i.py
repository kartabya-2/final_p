from moviepy.editor import VideoFileClip
import cv2



def main():
  dimen = max_co()
  if dimen is not None:
    l,h = dimen[0],dimen[1}
    print(f"So the video has {l}x{h} res")
    r_o_i(dimen[2])
    

def max_co():
  try:
    clip = VideoFileClip(input("Give me Path"))
    frame_rate = clip.fps
    frame_number = int(frame_rate * 3)
    frame = clip.get_frame(frame_number)
  except FileNotFoundError:
    print(f"Error: Video file not found.")
    return None
 max_x,max_y = clip.size
  clip.close()
  return [max_x-1, max_y-1, frame]# Adjust for zero-based indexing
  
def r_O_i(frame):
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  
  
  
  


if __name__ == "__main__":
  main()





