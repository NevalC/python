class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL_BEFORE_0: int = 1
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        '''
        Initializes attributes.
        '''
        self.__status: bool = False
        self.__muted: bool = False                             # Used only in volume functions
        self.__volume: int = Television.MIN_VOLUME            # Used only in volume functions
        self.__channel: int = 0                               # Used only in channel functions
        self.__channel_list: list = [0,1,2,3]                  # Used only in channel functions

    def power(self) -> None:
        '''
        Function to turn tv on or off.
        '''
        if self.__status == False:
            self.__status = True
            print('on')
        else:
            self.__status = False
            print('off')

    def mute(self) -> None:
        '''
        Function to mute tv.
        '''
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                print('sound off')
            else:
                self.__muted = False
                print('sound on')

    def channel_up(self) -> None:
        '''
        Function to go up channel list.
        '''
        if self.__status:
            try:
                if self.__channel <= Television.MAX_CHANNEL:
                    self.__channel += 1
                    print(f'channel {self.__channel_list[self.__channel]}') # Counting up, skipping zero
            except IndexError:
                self.__channel = 0
                print(f'channel {self.__channel_list[self.__channel]}')     # Begin counting up again from 0

    def channel_down(self) -> None:
        '''
        Function to go down channel list.
        :return:
        '''
        if self.__status:
            try:
                if self.__channel >= Television.MIN_CHANNEL_BEFORE_0:
                    self.__channel -= 1
                    print(f'channel {self.__channel_list[self.__channel]}')  # Counting down to 0
                elif self.__channel == 0:
                    self.__channel = 4
                    print(f'channel {self.__channel_list[self.__channel]}')  # Setting channel attribute to 4 to raise exception
            except IndexError:
                self.__channel = Television.MAX_CHANNEL
                print(f'channel {self.__channel_list[self.__channel]}')      # Counting down from 3

    def volume_up(self) -> None:
        '''
        Function to go up volume.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                print(f'volume {self.__volume}')         # Counts up to 2 and resets to 0 if going higher

    def volume_down(self) -> None:
        '''
        Function to go down volume.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                print(f'volume {self.__volume}')        # Counts down to 0 and resets to 2 if going lower
