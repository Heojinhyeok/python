class Elevator:


    def decide_action(self):
        #일단 시작점으로
        if not self.isStarted and not self.src == self.dest:
            if self.floor < self.src:
                self.status = "UPWARD"
                self.floor += 1
                return "UP"
            elif self.floor > self.src:
                self.status = "DOWNWARD"
                self.floor -= 1
                return "DOWN"
            else:
                self.status = "STOPPED"
                self.isStarted = True
                return "STOP"

        # 탈 사람, 내릴 사람
        to_enter = [call for call in self.calls if call['start']==self.floor]
        to_exit = [call for call in self.passengers if call['end']==self.floor]

        # 내리거나 타야할 층에 도착
        if (self.status == "UPWARD" or self.status == "DOWNWARD") and (to_enter or to_exit):
            self.status = "STOPPED"
            return "STOP"
        # 문을 연다
        elif self.status == "STOPPED" and (to_enter or to_exit):
            self.status = "OPEND"
            return "OPEN"
        # 열려있고 아직 탈 사람이 있다
        elif self.status == "OPEND" and to_enter:
            ret = dict()
            self.passengers.extend(to_enter)
            self.calls = [call for call in self.calls if call not in to_enter]
            ret["ENTER"] = [x['id'] for x in to_enter]
            return ret
        # 열려있고 아직 내릴 사람이 있다
        elif self.status == "OPEND" and to_exit:
            ret = dict()
            self.passengers = [passenger for passenger in self.passengers if passenger not in to_exit]
            ret["EXIT"] = [x['id'] for x in to_exit]
            return ret
        # 열려있고 다 내렸다
        elif self.status == "OPEND" and not (to_enter or to_exit):
            self.status = "STOPPED"
            if self.floor == self.dest:
                self.src = self.dest = 0
                self.isStarted = False
            return "CLOSE"
        # 한 번의 여정이 끝났다.
        elif self.src == self.dest:
            return "STOP"
        # 타거나 내리려는 사람 없이 이동중
        else:
            #print("what is this : ",self.src, self.dest, self.floor, self.status)
            if self.src < self.dest:
                self.status = "UPWARD"
                self.floor += 1
                return "UP"
            else:
                self.status = "DOWNWARD"
                self.floor -= 1
                return "DOWN"
