from moviepy.editor import VideoFileClip

def max_co():
  try:
    clip = VideoFileClip(input("Give me Path"))
  except FileNotFoundError:
    print(f"Error: Video file not found.")
    return None

  max_x,max_y = clip.w - 1,  clip.h - 1  # Adjust for zero-based indexing
  clip.close()
  return max_x, max_y



def main():
  dimen = max_co()
  if dimen is not None:
    l,h = dimen
    print(f"So the video has {l}x{h} res")






