import time
import busio
import board
import adafruit_amg88xx
 
amg, err := amg8833.NewAMG8833(&amg8833.Opts{
  Device: "/dev/i2c-1",
  Mode:   amg8833.AMG88xxNormalMode,
  Reset:  amg8833.AMG88xxInitialReset,
  FPS:    amg8833.AMG88xxFPS10,
})
if err != nil {
  panic(err)
}

ticker := time.NewTicker(1 * time.Second)

for {
  grid := amg.ReadPixels()
  fmt.Println(grid)
  <-ticker.C
}
