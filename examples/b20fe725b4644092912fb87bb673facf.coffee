#format 1.0
#name NUM_IV-9
#id b20fe725b4644092912fb87bb673facf
#desc Numitron IV-9 pinout

footprint = () ->
  name = new Name 6.5
  value = new Value -6.5
  cpad1 = new RoundPad 0.75, 1.0
  cpad1.name = '1'
  cpad1.shape = 'disc'
  cpad1.x = 0
  cpad1.y = -3.675
  cpad2 = new RoundPad 0.75, 1.0
  cpad2.name = '2'
  cpad2.shape = 'disc'
  cpad2.x = 2.345
  cpad2.y = -2.79
  cpad3 = new RoundPad 0.75, 1.0
  cpad3.name = '3'
  cpad3.shape = 'disc'
  cpad3.x = 3.675
  cpad3.y = -0.655
  cpad4 = new RoundPad 0.75, 1.0
  cpad4.name = '4'
  cpad4.shape = 'disc'
  cpad4.x = 3.425
  cpad4.y = 1.5
  cpad5 = new RoundPad 0.75, 1.0
  cpad5.name = '5'
  cpad5.shape = 'disc'
  cpad5.x = 1.79
  cpad5.y = 3.155
  cpad6 = new RoundPad 0.75, 1.0
  cpad6.name = '6'
  cpad6.shape = 'disc'
  cpad6.x = -0.615
  cpad6.y = 3.675
  cpad7 = new RoundPad 0.75, 1.0
  cpad7.name = '7'
  cpad7.shape = 'disc'
  cpad7.x = -2.655
  cpad7.y = 2.425
  cpad8 = new RoundPad 0.75, 1.0
  cpad8.name = '8'
  cpad8.shape = 'disc'
  cpad8.x = -3.675
  cpad8.y = 0.27
  cpad9 = new RoundPad 0.75, 1.0
  cpad9.name = '9'
  cpad9.shape = 'disc'
  cpad9.x = -3.175
  cpad9.y = -1.885
  label5 = new Label 'IV-9'
  label5.x = 0
  label5.y = 0.135
  label5.dy = 1.27
  silk1 = new Line 0.127
  silk1.x1 = -2.0
  silk1.y1 = -5.0
  silk1.x2 = 2.0
  silk1.y2 = -5.0
  silk2 = new Line 0.127
  silk2.x1 = -2.25
  silk2.y1 = -4.75
  silk2.x2 = 2.25
  silk2.y2 = -4.75
  silk3 = new Circle 0.127
  silk3.x = 0.0
  silk3.y = 0.0
  silk3.r = 5.6335
  silk4 = new Circle 0.127
  silk4.x = 0.0
  silk4.y = 0.0
  silk4.r = 2.8135
  [name, value, cpad1,cpad2,cpad3,cpad4,cpad5,cpad6,cpad7,cpad8,cpad9,label5,silk1,silk2,silk3,silk4]
