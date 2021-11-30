from camNativeLib.camNativeSDK import *
from camNativeLib.camEnum import *


class PTZControl(MouseEvent):
    MouseEvent = None
    sdk = HKSdkApi()
    sdk.add_dll()
    sdk.NET_DVR_Init()
    sdk.NET_DVR_Login_V40()

    while True:
        if MouseEvent == "UP_LEFTPressed":
            sdk.NET_DVR_PTZControl_Other(UP_LEFT, PTZ_CONTROL_START)
        if MouseEvent == "UP_LEFTReleased":
            sdk.NET_DVR_PTZControl_Other(UP_LEFT, PTZ_CONTROL_STOP)

        if MouseEvent == "UP_RIGHTPressed":
            sdk.NET_DVR_PTZControl_Other(UP_RIGHT, PTZ_CONTROL_START)
        if MouseEvent == "UP_RIGHTReleased":
            sdk.NET_DVR_PTZControl_Other(UP_RIGHT, PTZ_CONTROL_STOP)

        if MouseEvent == "DOWN_LEFTPressed":
            sdk.NET_DVR_PTZControl_Other(DOWN_LEFT, PTZ_CONTROL_START)
        if MouseEvent == "DOWN_LEFTReleased":
            sdk.NET_DVR_PTZControl_Other(DOWN_LEFT, PTZ_CONTROL_STOP)

        if MouseEvent == "DOWN_RIGHTPressed":
            sdk.NET_DVR_PTZControl_Other(DOWN_RIGHT, PTZ_CONTROL_START)
        if MouseEvent == "DOWN_RIGHTReleased":
            sdk.NET_DVR_PTZControl_Other(DOWN_RIGHT, PTZ_CONTROL_STOP)

        if MouseEvent == "PAN_LEFTPressed":
            sdk.NET_DVR_PTZControl_Other(PAN_LEFT, PTZ_CONTROL_START)
        if MouseEvent == "PAN_LEFTReleased":
            sdk.NET_DVR_PTZControl_Other(PAN_LEFT, PTZ_CONTROL_STOP)

        if MouseEvent == "PAN_RIGHTPressed":
            sdk.NET_DVR_PTZControl_Other(PAN_RIGHT, PTZ_CONTROL_START)
        if MouseEvent == "PAN_RIGHTReleased":
            sdk.NET_DVR_PTZControl_Other(PAN_RIGHT, PTZ_CONTROL_STOP)

        if MouseEvent == "TILT_UPPressed":
            sdk.NET_DVR_PTZControl_Other(TILT_UP, PTZ_CONTROL_START)
        if MouseEvent == "TILT_UPReleased":
            sdk.NET_DVR_PTZControl_Other(TILT_UP, PTZ_CONTROL_STOP)

        if MouseEvent == "TILT_DOWNPressed":
            sdk.NET_DVR_PTZControl_Other(TILT_DOWN, PTZ_CONTROL_START)
        if MouseEvent == "TILT_DOWNReleased":
            sdk.NET_DVR_PTZControl_Other(TILT_DOWN, PTZ_CONTROL_STOP)

        if MouseEvent == "ZOOM_INPressed":
            sdk.NET_DVR_PTZControl_Other(ZOOM_IN, PTZ_CONTROL_START)
        if MouseEvent == "ZOOM_INReleased":
            sdk.NET_DVR_PTZControl_Other(ZOOM_IN, PTZ_CONTROL_STOP)

        if MouseEvent == "ZOOM_OUTPressed":
            sdk.NET_DVR_PTZControl_Other(ZOOM_OUT, PTZ_CONTROL_START)
        if MouseEvent == "ZOOM_OUTReleased":
            sdk.NET_DVR_PTZControl_Other(ZOOM_OUT, PTZ_CONTROL_STOP)

        if MouseEvent == "ChangeCamera":
            break

    sdk.NET_DVR_Logout()

