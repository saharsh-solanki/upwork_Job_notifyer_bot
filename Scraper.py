import requests

class UpworkScraper:
    def __int__(self):
        self.headers = self.GetHeader()
        self.cookie_data = None

    def GetHeader(self):
        headers = {
            'authority': 'www.upwork.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'x-odesk-user-agent': 'oDesk LM',
            'vnd-eo-trace-id': '70052122195f85a2-SEA',
            # 'authorization': 'Bearer oauth2v2_3cfdcebf98e2953902e5213ef001bbe4',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?1',
            'x-requested-with': 'XMLHttpRequest',
            'vnd-eo-parent-span-id': '0239a1c8-1f13-44c4-9834-49d73596728b',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
            'vnd-eo-span-id': 'cbb8d314-cec4-456d-8cd2-ad80214b97ba',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.upwork.com/nx/find-work/most-recent',
            'accept-language': 'en-GB,en;q=0.9',
            'cookie': self.cookie_data
            # 'cookie': '_pxhd=eLsEvZscMdkmlRzBh18mJNYcux-3gUjZpja97pRC/1PXyKrvUpmadQpQLDORq//ZKvlTaJzyLOw-TjNt2VgEEw==:XdlQ9mrK97Tgwpw94/UeXgT9zASBWLu5fQXHfWaD3Y07MpZDMVGGfWon-O6EDG8b686nsD6noevHFT8Wve1RavIsLsD8e51RyyfC3os2n5M=; visitor_id=110.224.174.56.1650701000616000; lang=en; lang=en; visitor_gql_token=oauth2v2_5ee39db73aff197c4e8181fedebc16c7; cookie_prefix=; cookie_domain=.upwork.com; pxcts=d8729655-c2db-11ec-9bda-454a656f4c4d; _pxvid=d7357972-c2db-11ec-bf6e-516f45617a42; _gcl_au=1.1.1026673884.1650701006; _sp_ses.2a16=*; device_view=full; _gid=GA1.2.907839485.1650701009; G_ENABLED_IDPS=google; _hp2_ses_props.2858077939=%7B%22r%22%3A%22https%3A%2F%2Fwww.upwork.com%2F%22%2C%22ts%22%3A1650701008486%2C%22d%22%3A%22www.upwork.com%22%2C%22h%22%3A%22%2Fab%2Faccount-security%2Flogin%22%7D; _rdt_uuid=1650701010422.69610c9b-6f29-4028-8a64-7028f38f52b5; __pdst=fdc4804ceadc4e5487ea820242f790cc; IR_gbd=upwork.com; _dpm_ses.5831=*; _fbp=fb.1.1650701010990.390737900; prodperfect_session={%22session_uuid%22:%22349559dc-eae6-4d57-8daf-deadc0ecaeba%22}; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+23+2022+13%3A33%3A33+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=79a9ec19-4e00-4776-a00c-32c21c37bb95&interactionCount=1&landingPath=https%3A%2F%2Fwww.upwork.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; fs_uid=rs.fullstory.com#P8EM8#6085055002566656:5791063987838976/1682237013; AWSALB=WDvC41YavmCC9zBcVQ538Bz0PabGkwHAuM5kiUxkD5Nyu2tBzAbFQCNdW5nlxHpkca9+4GwXqV/vHFF+20nKmlz7UT4R1OdFb+DaP+oBx+kc1vJw+gfCGnun8lM0; AWSALBCORS=WDvC41YavmCC9zBcVQ538Bz0PabGkwHAuM5kiUxkD5Nyu2tBzAbFQCNdW5nlxHpkca9+4GwXqV/vHFF+20nKmlz7UT4R1OdFb+DaP+oBx+kc1vJw+gfCGnun8lM0; spt=dd16e451-3ae4-42bc-b7d1-0c8f3d7050d4; _clck=1o6f6na|1|f0v|0; recognized=b3e8bc89; console_user=b3e8bc89; user_uid=1517776442924953600; master_access_token=99ef3287.oauth2v2_cdb5fb7d05b8b27e644bce5713f4b52d; oauth2_global_js_token=oauth2v2_3cfdcebf98e2953902e5213ef001bbe4; SZ=da811304ec405769966deabb5b1f5d8db7cbd967a2fc022ad249c55c3efe8eb7; current_organization_uid=1517776442924953601; company_last_accessed=d1014476434; user_oauth2_slave_access_token=99ef3287.oauth2v2_cdb5fb7d05b8b27e644bce5713f4b52d:1517776442924953600.oauth2v2_b61ee300a5e6c2076af88b65b98f1514; visitor_signup_gql_token=oauth2v2_27b564a66857b8b84ec5ed74a83253f6; odesk_signup.referer.raw=https%3A%2F%2Fwww.upwork.com%2Fnx%2Fsignup%2Fverify-email%2Ftoken%2FwAemGoEoeC; clob_signup_cookie=Hz7zFnTfOVlOwQcPd6BFMjwcWb1hwZ8ve6GfBrUGia%2FhmRh9ribYelcVMR1HRHU7ELotNC0rvkkjNE29r06cFpAndpdsYRDJdWThZmN49gULUcimy92TZ8UPbBAavTKEQCzPdHpgA9jB2NcPf6Dy15RHw%2Br0reWSSPTTEG5Vy3Tzo%2BVR1UPR0c7nzf8w2%2BMlcSli3TERTVrsBAQUYY9%2FZRZySvvcCHjYzJ81xnR064hXehqEGYN39r%2BGYsDPn%2BGhAHJhczk3eg%3D%3D; _dc_gtm_UA-62227314-1=1; _dc_gtm_UA-62227314-13=1; channel=other; _px3=f8b1682e6879722796eef0e06ca6c96859392007e526890bff96304fadf6ed40:k6LkRda/My+7N8Ll25hCrON3eSniW0k1BLNkSmoGZYZEMQqsu9ZxTANH+O0Ecb19TBfQtSWfG1YTIXsY80P1jQ==:1000:cXmFidmjwwD29U8SyTFsQSyvVgvIZof0uyEeuaU3mGG7MfqQ8G09ElKJ1Tpe2cD8/TtCffmmJMKo7U6e+LhURW7bkXP0PwXeoANLeNfI80yPv9ppp/1o/yxQX8rWxeFT60kHYpeojBIlnb8ynxUZMTpqvVVJYH17uotPT7zsgQ3zwb8weHJunigbTIBHetO8J7YqhZkt20cY3INGzfZUuQ==; __cfruid=15a1e0106c87071220e41bd546f086409ab1280b-1650701500; __cf_bm=uGeAcd9K7TJi0oDLaEt.omcDHFnBxCNE0PNRk.ZH4_A-1650701500-0-AaEpD/ppYnJIKyBXff7cIcofbV298k4h1xDGWDNFKdgMYRtJK7Kc9mlPjD6tKYRREG2Beev4UYzEcoSPrhXC0K8=; XSRF-TOKEN=a947bab62c5d84d5d377dcdcc44b5009; _ga_KSM221PNDX=GS1.1.1650701007.1.1.1650701500.0; _uetsid=dd512fb0c2db11ecaa6b9530e064f632; _uetvid=dd516e00c2db11ecabc3cba996d2b7b3; _hp2_props.2858077939=%7B%22container_id%22%3A%22GTM-WNVF2RB%22%2C%22user_context%22%3A%22freelancer%22%2C%22user_logged_in%22%3Atrue%7D; _dpm_id.5831=543cd353-50a8-4664-b6a6-82d95b0df9bf.1650701011.1.1650701502.1650701011.85244b06-30c4-4fa1-b12d-eac970bc6bc9; _ga=GA1.2.1949363637.1650701007; IR_13634=1650701501703%7C0%7C1650701501703%7C%7C; _hp2_id.2858077939=%7B%22userId%22%3A%223947439559923101%22%2C%22pageviewId%22%3A%228525165571811771%22%2C%22sessionId%22%3A%228701650202551581%22%2C%22identity%22%3A%221517776442924953600%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _clsk=bb0j36|1650701503493|10|0|d.clarity.ms/collect; enabled_ff=u0021CI10270Air2Dot5QTAllocations,CI11132Air2Dot75,OTBnrOn,CI9570Air2Dot5,u0021CI12577UniversalSearch,u0021SSINav,u0021CI10857Air3Dot0,u0021air2Dot76,u0021air2Dot76Qt,u0021OTBnr; _sp_id.2a16=51c38286-2d94-4ac7-a600-6f5428291f3f.1650701006.1.1650701505.1650701006.740ec704-43a4-4d00-b7da-9114647dc00e; company_last_accessed=d1014476434; current_organization_uid=1517776442924953601; visitor_id=110.224.174.56.1650701000616000; enabled_ff=!air2Dot76,!OTBnr,CI11132Air2Dot75,OTBnrOn,!SSINav,CI9570Air2Dot5,!CI10270Air2Dot5QTAllocations,!air2Dot76Qt,!CI12577UniversalSearch,!CI10857Air3Dot0'
        }
        return  headers

    def CloseBrowser(self):
        self.driver.quit()


    # def GenerateCookieFile(self):
    #     cookies = self.driver.get_cookies()
    #     CookieToBeWrite = ""
    #     file = open("cookies.txt", "w")
    #     cookie = ""
    #     for cookie in cookies:
    #         CookieToBeWrite = CookieToBeWrite + str(cookie["name"] + "=" + cookie["value"] + ";")
    #         # file.write( CookieToBeWrite)
    #         cookie += CookieToBeWrite
    #     file.write("'"+cookie+"'")
    #     file.close()
    #     self.cookie = True
    #     print("Cookie Generated Successfully")

    # def setAndCheckCookie(self):
    #     files = open("cookies.txt", "r")
    #     cookie = files.read()
    #     if cookie:
    #         self.cookie_data = cookie
    #         return True
    #     else:
    #         return False

    def GetCookie(self):
        return self.cookie_data

    def set_cookie(self,cooki):
        self.cookie_data = cooki

    def FetchJobs(self):
        url = "https://www.upwork.com/ab/find-work/api/feeds/embeddings-recommendations?paging=0%3B10"
        payload = {}
        headers = self.GetHeader()
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            response = response.json()
            if type(response) == str:
                return  False
            return response
        except:
            return False