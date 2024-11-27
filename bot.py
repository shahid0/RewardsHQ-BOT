import requests
import json
import os
from colorama import *
from datetime import datetime
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class RewardsHQ:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'api-rewardshq.shards.tech',
            'Origin': 'https://rewardshq.shards.tech',
            'Pragma': 'no-cache',
            'Referer': 'https://rewardshq.shards.tech/?tgWebAppStartParam=daily-spin',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}RewardsHQ - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def auth_login(self, query: str):
        url = 'https://api-rewardshq.shards.tech/v1/auth/login'
        data = json.dumps({"telegramInitData":query})
        self.headers.update({
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, data=data)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']['accessToken']
            else:
                return None
        else:
            return None
        
    def users_info(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/users'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def point_logs(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/point-logs'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def users_level(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/tasks/level'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def streak_login(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/users/streak-login'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def farming_info(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-earn-hour'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def start_farming(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-earn-hour'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.put(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def refferal_data(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-referral/list'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def user_refferal(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-referral'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def refferal_list(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-referral/list-boost'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def nudge_all(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-referral/boost-all'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.put(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def nudge_one(self, token: str, reff_id: str):
        url = f'https://api-rewardshq.shards.tech/v1/user-referral/boost/{reff_id}'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.put(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def claim_freespin(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-spin-logs/share-story'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def spin_logs(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-spin-logs'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def do_spin(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/user-spin-logs'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.put(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def achievements(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/tasks/one-time'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def claim_achievements(self, token: str, achievement_id: str, target: int):
        url = f'https://api-rewardshq.shards.tech/v1/tasks/one-time/{achievement_id}/{target}'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def campaigns(self, token: str):
        url = 'https://api-rewardshq.shards.tech/v1/campaigns?page=1&limit=10&keyword='
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def campaigns_lists(self, token: str, campaign_ids: list):
        endpoint = '&'.join([f'campaignIds[]={campaign_id}' for campaign_id in campaign_ids])
        url = f'https://api-rewardshq.shards.tech/v1/user-quest/list?{endpoint}'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def complete_campaigns(self, token: str, campaign_id: str):
        url = f'https://api-rewardshq.shards.tech/v1/user-quest/{campaign_id}'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.put(url, headers=self.headers, json=data)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def tasks(self, token: str, task_type: str = None):
        base_url = 'https://api-rewardshq.shards.tech/v1/tasks'
        if task_type == "basic":
            url = f'{base_url}/basic-tasks'
        elif task_type == "partner":
            url = f'{base_url}/partner-tasks'
        else:
            url = base_url

        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.get(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def complete_daily(self, token: str, task_id: str):
        url = f'https://api-rewardshq.shards.tech/v1/tasks/do-task/{task_id}'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers, json=data)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
        
    def complete_other(self, token: str, task_type: str, task_id: str):
        url = f'https://api-rewardshq.shards.tech/v1/tasks/{task_type}-tasks/{task_id}'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        response = self.session.post(url, headers=self.headers)
        result = response.json()
        if response.status_code in [200, 201]:
            if result and result['message'] == 'Success':
                return result['data']
            else:
                return None
        else:
            return None
    
    def process_query(self, query: str):

        token = self.auth_login(query)
        if not token:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if token:
            user = self.users_info(token)
            if user:
                points = self.point_logs(token)
                level = self.users_level(token)
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['firstName']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {points['point']} Points {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Level{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {level['level']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {level['xp']} XP {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                check_in = self.streak_login(token)
                if check_in:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} Streak {check_in['streak']} Day {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {check_in['nextPointBonus']} Points {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                farming = self.farming_info(token)
                if farming is None:
                    start = self.start_farming(token)
                    if start:
                        end_time = start['endTime']
                        end_time_wib = datetime.fromtimestamp(end_time).astimezone(wib).strftime('%x %X %Z')
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ End at{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {end_time_wib} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    end_time = farming['endTime']
                    end_time_wib = datetime.fromtimestamp(end_time).astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ End at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {end_time_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                self.refferal_data(token)
                refferal = self.user_refferal(token)
                if refferal and refferal > 0:
                    nudge = self.nudge_all(token)
                    if nudge:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Success to Nudge {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        reff_lists = self.refferal_list(token)
                        if reff_lists:
                            completed_nudge = False
                            for reff in reff_lists:
                                reff_id = reff['user']
                                nudge = self.nudge_one(token, reff_id)
                                if nudge:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} ID {reff_id} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Is Success to Nudge{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                else:
                                    completed_nudge = True

                                time.sleep(1)

                            if completed_nudge:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} No Available Refferal to Nudge {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} List Data Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Have Yet {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                free_ticket = self.claim_freespin(token)
                if free_ticket:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Free Ticket{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Free Ticket{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                spin_logs = self.spin_logs(token)
                if spin_logs:
                    ticket = spin_logs['numberSpin']
                    if ticket > 0:
                        while ticket > 0:
                            spin = self.do_spin(token)
                            if spin:
                                ticket -= 1
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Spin{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewrad{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {spin['point']} Points {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {spin['xp']} XP {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {spin['usdt']} USDT {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {ticket} Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                break

                            time.sleep(1)

                        if ticket == 0:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Spin{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} No Available Ticket {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Spin{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} No Available Ticket {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Spin{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                achievemets = self.achievements(token)
                if achievemets:
                    completed = False
                    for achievement in achievemets:
                        achievement_id = achievement['_id']
                        progress = achievement['progress']
                        title = achievement['metadata']['name']
                        streak = achievement['metadata']['streak']
                        logs = achievement.get('logs', [])

                        eligible_streaks = [
                            s for s in streak
                            if s['target'] <= progress and not any(
                                log['metadata']['target'] == s['target'] for log in logs
                            )
                        ]

                        if eligible_streaks:
                            for streak_item in eligible_streaks:
                                target = streak_item['target']
                                if 'point' in streak_item:
                                    reward_type = "Points"
                                    reward = streak_item['point']
                                elif 'spin' in streak_item:
                                    reward_type = "Ticket"
                                    reward = streak_item['spin']
                                else:
                                    reward_type = "Unknown"
                                    reward = None
                            
                                claim = self.claim_achievements(token, achievement_id, target)
                                if claim:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Achievement{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewrad{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {reward} {reward_type} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Achievement{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                        else:
                            completed = True

                    if completed:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Achievement{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} All Eigible Reward {Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Achievement{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                campaigns = self.campaigns(token)
                if campaigns:
                    campaign_ids = [campaign['_id'] for campaign in campaigns if '_id' in campaign]
                    
                    if campaign_ids:
                        campaign_lists = self.campaigns_lists(token, campaign_ids)
                        if campaign_lists:
                            completed_campaign = False
                            for campaign_list in campaign_lists:
                                for campaign in campaign_list:
                                    if '_id' in campaign and (not 'status' in campaign or campaign['status'] != 'completed'):
                                        complete = self.complete_campaigns(token, campaign['_id'])
                                        if complete:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Campaign{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {campaign['name']} {Style.RESET_ALL}"
                                                f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                        else:
                                            self.log(
                                                f"{Fore.MAGENTA+Style.BRIGHT}[ Campaign{Style.RESET_ALL}"
                                                f"{Fore.WHITE+Style.BRIGHT} {campaign['name']} {Style.RESET_ALL}"
                                                f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                            )
                                        time.sleep(1)
                                    else:
                                        completed_campaign = True

                            if completed_campaign:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Campaign{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} All Eigible Task {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Campaign{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Campaign{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                task_types = [None, 'basic', 'partner']
                for task_type in task_types:
                    tasks = self.tasks(token, task_type)
                    if tasks:
                        completed_task = False
                        for task in tasks:
                            task_id = task['_id']
                            completed = task['isCompleted']
                            can_claim = task['isCanClaim']

                            if task and not completed and can_claim:
                                if task_type is None:
                                    complete = self.complete_daily(token, task_id)
                                else:
                                    complete = self.complete_other(token, task_type, task_id)

                                if complete:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['metadata']['name']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['xp']} XP {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['metadata']['name']} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                time.sleep(1)
                            else:
                                completed_task = True

                        if completed_task:
                            if task_type == None:
                                title = 'Daily'
                            elif task_type == 'basic':
                                title = 'Basic'
                            elif task_type == 'partner':
                                title = 'Partner'

                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} All Eigible {title} Task {Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
            
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            # while True:
            self.clear_terminal()
            self.welcome()
            self.log(
                f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
            )
            self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

            for query in queries:
                query = query.strip()
                if query:
                    self.process_query(query)
                    self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                    time.sleep(3)

            # seconds = 1800
            # while seconds > 0:
                # formatted_time = self.format_seconds(seconds)
                # print(
                    # f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                    # f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                    # f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                    # end="\r"
                # )
                # time.sleep(1)
                # seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] RewardsHQ - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = RewardsHQ()
    bot.main()
