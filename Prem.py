# Kalo Mau Recode Izin Dulu Bos!
import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnpGZkF0d0hNbDUzc3pzQTR0ZHZOOHZra09RQkFHUXdEN3dKZ2lTNEp2aUE3d0RlVHp1M1hrMTJCNHNCdGdYZTJZSllMVTRuMFBKZG1LZjdpNVNJc1ZIUm9ES2NVTGJlVGhLYkNWMkVzV0o3TWhKcWxKNXVGS2JWQ29sSjVXNk9LOUtTaWw1TGVueS85MHpzN1BMeFpGbjZTS0MrODgvL1pydW51Ny8vLzd1ditjUGhLcC9idmlkZzkvLzZRZENCQ0ltaGFpZ2lxcXdLeEZwVDN3a2loQzJMTlEvZFgyQXlXL3B5ZGNFNFErcVMyazBTOUZsVjdrVWRoV2pJcnRLVVlsZFhWRVh1N3FqYm5iMVJEM3M2bzE2NFNvbDYxSytxRS9Fdks1a2Zjb2Y5VFBlblF5a0F0R0FLQ1NFYUFQeFJCdUpOOXBFNnFMTnhCZHRJZlhSVnVMZmJVc0lhdVA3d25zaUNid25tbHdEY0syTWE3UzVKcHRyQnE2WmNTMTJXS3NkMWdaY2k1Mk94N2JiWWExMldNY0xwdXQ4d1hSZEwxaS83dmZFUFRIYW5oOVF2ZXNkdTUya1owOGt2UnNTL2FicTNlMGlmWHZ3NXN5WWZqUG1YN0tZQVl5NUo2VGRvb0IvOTRWOEM3enRibklBU3V0UmU4bEJjdWlSdE51bjlxejNteW1QdVFWMTRGMXh1MUVVb2dkRUlkK2pIc1Rha0dic1pTSXp2cFh4aDlVRDd3dFA2aCt4ZlBmaHZVWVB2SFlnN2VIWFRYRlRJSVBSUStRSU9mcFpJU3FUWTJRSXJvZkpjVElNMTBFeVFrYmhlb1NjSUNmaGVwU01rWEc0SGlOQkVvTHJFQW1UQ0Z5UGt3a3lDZGRoTWtXbTRUcHlSU0F6WlBhekFwbDlKRVZIeVJ3NUJhRW4xSk5rZmtONlY2U2Z6eDh5KytFMDd3Y0llNFAxeEFMcm84T1BCS3d0am5KSDZJbHlxTm42dDgzVzkzNjgxbU1KanZiRDNjZ1pQcFZHeEdMYm5UV3FLdVIySnBPOHRLWEdjMGFHUW1qemhVdzZyY1lOTFpPK1JDa0w4bVdUaXJHYW9hbDhYZjlyNGZtNXNNVkVMR2JDWXFZdFppWlZGUExINUZnczV2akpzc1hLd0pvQi92eFFBVzVlNTc5WVFaWmZEOHB5QWFJTE12L2pBU3lkSEFOV0RrSWNSTHdlQk1MLzg3UXNBTlBGV0ZEc2RYZ1c4dXdHV0x3UFdnSCtrdmhhU1Z3b2lXL2tRS29JMzM3cmk1L1FmMzlSM01xM3lvczVZeTFENVZNeXplVFhsQTEvdmtlK3JNVFZsVXhtQXdMUDhkRHhyZTI4UDM5UXZwYldEU1ZCbFZRNUtwWlpYZFhpbXBMMDU2S2ZhSDJqN291S29Wek8rMU1iUktNeTNrVHJYbGIxWE5MUTg0MDgwTHJkWERPTXJINHFHRlN5Mm5pV1pyYTI5VGhWc3VwNFBKTUtQb3dFejFMMVFVN1ZqUVdpNlRDS3RqR0pwdXBEY0RVeThVeHlRYy9FTi9USklVTkxxWm1jc1JBTzRiK2hlQ2FYTnVqMmdwSk1EdWw2a2wyVmRDYTluZElNRmxwcXdXb0ZiL1BpeG8wdG95aHVsc1RESlZGV3VrUkJ1Sm5KYThta0Vwd2FEOG5ETjdSMGJtdGVYa3dUbXRHSUhJN015N2UxTFRVcFR5bnkrWnlXSk1IbDIrSEY4VWc0SEE1Qmh0REV2THo1Y0VSZXpHYVQ2ajExNWJwbUJLY21ac1lucHVYaDYxZnYzTHh4VWs1cUc2cDhSWTF2WkVia1YxU3F3MlFKVHNLakxxelJURW9OemsyUGg4WW5wNmNueCtjaThzM01pcFpVNVdWbFZhR2FWVkQ1L1ViQ21EZzBIZ21OaHlkbTdFb09UNFNEV05ISlNJaGt0WGs1SEpvTmJVWGczN3g4SlpOSkpOVmdnbDNLVFptWFZ4UzZvaHJscTVxTzNWMmVseWNtWm1jaUU1T3prWkY0dGZKdGg5OEZWSjMvQWZvcy95MUQyQldKaUNMSWtBd1hDQlhKY0FOMUdSNmdic1o3R084MXc3MUE2OHh3NUgxUDJsQUFHWFhzanVlclp6elA1MmRwQTAvOGo4UWRvWURLdGVGelVxOUFHaDhLOU5Qd3pIS3VKa2V1NWljK1ZxcHZ0NTQwc05waFBWc1k1emRGcFFDQ3J0VUlGSVJISXBUMUcwYkRiaU5wNC9kNzBtNFRhZDhUZDBTam1YU1FUbEF3TFFYZXl0YjFOdEpWRU9FWjNVOWNSanZVcU9leFJIcmZsblk3OWdUUzF5dnNTSkNuMzh3am1EMVRydVdBbzVZSGVOc0tFam5ZSyt4Mjdna2dqZ04ydlEreHZGM2wyaHArbHN0bGRMUFdlbGc1eU11OHRUeVZXekI2dHYrSEtPeTRVUGp2bXlkUWNGVUlmMGovcG92MUNlTlErSThjdmxYMHhKT3FRa3VTMzArOThOWkw0aEhxZzJ2KzUrUmxMYW1zYlNocCthYWk1L0I2QWNTU3BzcUxHN20wWTdEQzZGUk95cmNWM2RBdzBaVmNXc0VyUzNVbmwxcFJrdkxkdEpIYmtHOWtFbHI2cFB3cFNNWXl5ZWZWWkM0bDMxVFRDZFZRMW5LYStRRGRVZmgxRlVxVmk2NHJLa3hta001bjgvVldOVTVSQkhrZkFMNFRucnFLTGlpRHRnSWZkVjI1ZEljMllCTUcrV01Xc1RvWE5ZWHkxbHhYNWZzZ1ZuSXI2dmo0ZVA3WUZrbU1aYkpxV3JhazFqWkdqcStvd1Z4NEp2cFNZbG1mVU83bkEwU1A1WFNWeGpTeWtHOTEzQXlQajU0ZG1mOUF4SzVyWnZMbkxzUm9CTVVQRFdEb01hdGdiVnl6MnNWRUlZakg0TU53RUV2U2d5VnZVRXV2Wm9KUHBaSWZROGFVaEpvMml0NDRhK3hUc1ZpM0Jub1pVaGJkR0cwK2kzY0ZGM1dqZWI5OFQwMUN5ZEEzeGZyVlhESVpTeXNwOVFNSisyS2cvSWJNL2x2T0VXVU4za0Zhb1NPOVJTbWpGNzM2dG02b3FhSW5TelY4OW9vQ1dwOFd4ZXRGOFhaUnZGcjBhT2xzemlpNlVUQVhQWHBTVmJORnQ3cWxHVVdYYnRDaVJGVW9BZ1pUZkszb1NkQk1EbUt4WjR1ZVRhb1phdEZueW4yZGRrR05pdlhZRHQ1Szk3cWVnV1NHWmlTaGlOVk1NcG5aTElvM2kvV1h0dUpxRm1ISGlEdmF1aFNDUC9ZUDFBRVNEQUl1WkljdVlSQW1DN0Z3bHR3TTRpbFk1RkxvcVVBWHNBb1NTUlE5S1J6ZEF5andEZ0tSUkw5NFJod1NXOFJ6WWdOY0o4V3I0cERVSkVaRTMxdlNoL1FzSkttUW1CNm54R3lBd2ZpdW1MLzRZNVdaRDU0ck0vZUxiM0hJMUZaYnByWlZ5MVFqc051d0o3enp6UjJ4SUJpTmp3VFMvbGpha1FyaWVoUHBBRW5YQ1pLeWVROWtET2t5V2dvdTB0M0w1ZSt2d0hPNXBHcDFTQ3JrZTJvK3Q3ZjgzTFJCK2xoWi9XWlp2N3R2V1FObVdUeWZBaElZOHgzaytmUi9TdzQ1N3dGNFN4VzlJVHQ2NDdBcHUxMWtFR1IzbTBOMnQ2UEJBTksvdzVUK1pSM1V5WjRhM0xkMlVKcFpVcjBsejkzdzk4aGw5ZTJmTENRTUxkSFBiSXFXQWVYUUZGMWdLSHlhaDl1YW9ycFd4M2lmM2JmeWRFT2V6NEYrY1Zmb2wyZmI0cTdTTCs0MzNhWitBWTdwbDZGYnRBa21CbTFHZ3VxRnRpQmhDdVpkTHAydktqU25neEpJbVVwbU1RczRhbHRlTkpTY2ZFUFQxYlN1blpTdkswbTROYU80NExxdUVDV1pVNml1T011NW13WHhTbFFVOHJlcG10SnlxWTlVT0dhSlhNc3c5VUhia09DTUJrMWpSbk5OUXp1UWRDSmgybVVLcE8yS0RvSk5IcllsdkMzZk9UemZJdU9wN1hHTkJLbWEwRUMwMHVCSWZtZy9wWFFIalMyQTh1bHRCUlFUUFlyUHVQV01kdHJjM0J3SE5KaGR5V3d4SmFJSFY5YTJIanhJeklhMjlVeHVLbXdFWDds'
love = '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'
god = 'RlFYTTN6b0l6U3phV3NXd09NMVcxTlBGbExXbUNzbURjRmlZUy9Ga0NaZFFVSzlJUE9sd3RZb2NvZlNoOXA2WFJGQzQvVnkxY2NOblRCamhyQ0hCMmZyd0FoK1ZxTVNlcXhFd1FFRFVzVHh0dzdSVVR0Y05SMDA1SFRidHMwNk1iSm1vSDZiRW5LdHNuZTNDSjhYMDFUWTkzSEpPMHI2YnA4VFhibThCcGV2UlhtQjdQOXlZWStLRW1hTmt3MlE5QnJKZ1dpUkpuYzFhUFVUVU9FOWhRYUVJMTdOVXZQc1VQRFducGVESkgxRmdaZU1TNCtiK0FNT0pqS1h3Mms4dldCTTNqZkhJN0xHTnJEcFdOZU50TU41V3NPWlVxckd3YjlTODlvMlE5VkZXVE9zNXF2YytlRTlPMWxPdlBWNDkvM083dnM4Yi83K1A0LzJiMWZqVGZCWDd1cnJUSHNTdU52TThSWHU4STl6L3BaU1hDNkxmakE0em44UTJHRDJpanZWdmRCQXAxeXhEVzYzZjlwSGxQSkMwYkVsMDFBdVkrWThQNzZMWEQ5eG1SYjNQNnZwZzdxNDFQcEVmV1BuRTdhMWVnUE9iaENSM3doS2ZtRXpyTkozeHAzeWQwUGVjSjNUV2UwQU5QK0JydWZwZDN4ZmNwdmJmS2Q2Y0psZWFPeUdiYmZua2FjWStoWXJhSmI0cm1iQU9PemJZK2MyK1ZiVmppdkN1S1lXN3dkOHMzdERYRmtLL2lNcFo4WVUzZHlHYTB0T0V2aWhGYzVYTEUzZEFlcWhBOGtXK1VyNnZvcXFQNVpmakhabkNwSHJKbU1ycGxRVHlWNk50TTVZWENwU2JUMXk5NElZdm8rVExmRVcyM25wZ3Q3MnpsMitMd3RNcmtVTkxuZVVtUmNrbExHeGhsbDdHMHNWOFpQQ0dVOFE0dlk2TFVJTitqbVhSQ3ZvYnVLU1BOdFhiUGl1SjVybjNMeWhqMWNOR2RWWXkxb2xmZDB0QXZ4VGJXMlpvYzN3aVR5dXRyRnBRdXU1U0ViSVJkUFlIcktLOHVJZ2Y5dHNBZFMveWlHOVNhKzhPS24rVCtRY1hQNWY1KytlZi8vcERIQnhQL3FNaHBCd2lDY3pqeEJmb0wxUk1mLzlWYkUvOFd2aEI1ZjhWbm9sYlhycHQ0MlBEMjdIcUpsM0YxajZvMmdzd3RvRHBUdkRkWTRqMS9aTCs5N0hzd3hIUWxtOFUxVkJTYithTXZzdnM3NHR0L2tiVDhUb04yUjFmTFRCVzNMOS9IMWlNR09BOXlrdDFWZEpMb1JBYy8veVBwSkpqVHZ1MUxNS2NGTnFmcnpOTHFIYVVoWDFjUXF1YTA4S1pnem1uZzJKejJQZFBGQS9LeVNuQXpDOWZCMXBSc1RyZTg1S3krNWVBVTJ6VGk1LzFYaHBuNzl0OXBhNlNQaU9ZcXMya0ExZ1JwM2cwVk4vTC9JdmFaajNXdE9RWWYxeHFEcUlET1lWSmNQVmNGUEc4UmxYQzc5Yk5DMUVWY3hBMVg2RkRpaGF1SDFNSEk4akhVR2hjZGhmamgxMmE5cDEvSFF4eGlRWWdKQ1pDOU1aRlIwR1RyN2wwUEhnb2hMcER2bC9NdHVHTnI3dDM2aUVROGdNUHFDK0s2M3p3MmNCVGVWSUM5S1Z4bTdUSDNWYjFzTDdXTzhUN0cxOWRhWmsxN3lvdXNSalB4NzdZa0JEellZZkJqRU43M21GSERqM2lZWVQ0N3JCRzROanRkdTNYc3d3enoyV0hOTmNwcmVXNTU5a0VNUjNrc2pCK1hNVHFZdjQ3WFhGcHFaZTNrQmxnN3RwYnBaUmNZblIzTUkrcDBQZ3Z0YThheXpEeWRqT2Q1dXZZSjczN1N5cDdWU1hwSTc5dmlPNUVkdDlFRmlQYzQ3bnp2ZGlQdWZGM2E4ZTdVRmVyZ3JoN2VtUWdZMmxmQSt4N2NWZCtUQ2o3UzN5MEFIZWdXRXU2ZGVqQnhld3ZDZXAvUlZmQVc2dmZjZ0hML25YTUhPMTNQL0o2YW5QdlhnS0NiSGEwOVVHNnRVd3ViZUJqVE5qblNObFdtNVdJUHZjVll2M3dyLytCSDBDOFRacjhNLzlEOTBsL3VsM2ZGQjRrYVBmUCtKOXN6Kzg2ZlF6d1ZVeHJ5TGNwOFk5dnNCVGZtOHNsUVEvNndwUXl5aW02b0sxcWF3WDJxYkFabjZmcVZHOVBoVjVqRFRKVk01QVlGcm1OenZ6SkVKZmsrRUpDNEVDL2ZxOTdWa0tQdVpiRDFPVTVpdU1OOUdSN0hyWlIza2J3SEpJZTdVTjkrNjZ2NVlRY0FRUy8rVkpZcE4vbFVGUUR4NTBNT3VGTTdKWWM3REZMaHZ3K09jSUViU0NsYnNjME0zY0F0RUxRK29xNXdaQ0xxWWZ2MjBicGxOYW5xaWthL2dIWDc4NWhsb0ZpWHpHU3lXanBSZENjQnNoVmRSRk81U1A4eWtyOGdWQ3dwMks0OWZBMmh2QTh4YWtsOXZwWGhYZ2RZeUxYdGwyeVZ3UUFTaW5DMnNGRDA2Tm1rWmlDY3lTYVZ1QnIxNnJtVkZBUzRkZlRSZGE5Q1Q0NzRuWTY0NVYxSjUrcWp0U3RwYlVDYXhGNlV0RFloN1YxSnh6cGwyVjRxMjB3VmU1Yzh3dHIwdERQYkRrdmxCWTJRdmNCcGI0UStDOTE4c1ppVzFveFk3S3VvZTM0UGlGZkV2eFp4VUR6RDlGNkRLRW0rSDN6a3orWDcvdjQvUUhWdVB5TEI1NkJCL3c4YTNENHc5WnJBOE9zUXBlOGQvSERJaS91cUh5OW5sNTN6cUpodjV2dFY0MVliNDI2SDBzWHBaRHN6ZngxaTNwWHlWd3V1aTNCOXc4dldISVU5QVFTWXVDdkIxVU5FZEdUYWRSVUFFcTI3ZCtvWVBKSU1FRjNNamNwSFhLQ0tmUVVQTThPWXhzZkZFWFFmTmhwUnRJRjZidG9UMEZrWXhGN0E0VTRsY29lcXg4Mm91QXMrVk1la0EvSzFvSVBWSHQ1MXMxMFJOK2w1N05xcEo3Mmt6eXkxdjdMVUxrRVRkL3hRZzFZVWxRVS9HU0FIM25idkJNaEJxR1ZnM1cwNkFRL25od3h4M1VVT01jVXZHVzFRa215VlJBNC9sc2pnMjlKdU8vQkhlZ1Z5RkFSMFE2R0JIQU4rQ1BoRzRJK2JmQlBBakRZM3F0ek9WV243S1JlbnBIT25FWDVOOXgxbkhJMHVNc3lPYVl3WVBVQkhHWCtDOFNjNTlEQzZIUEZqanZqeE1qelpOMDJ3dkd1MGI1cFFvZkc1YWNJRkZPZ1JoQWp3Sm9UMTN0MCs5alltV1BsODBhcVJUSklwNkt2K2NnelFSa1o1YnQ4ZVUwVHAvMFNtSy9yOVAvOUkrNzNkNnZkM3hlM1Y1L1Q4Z04zYUdjYnoxczdhdlRIZzZJMkJmWHErZHByS25xK2RwckxuYTZlcDd2a0ROWHQrN2dWNy9qZzU1ZWg1aVFhTWcrdUhkdnVoSjNyWTAyV2c4NHcvd2ZqVFR3Q0tzRFNIOTRSVlhHb2MzRDNDVDZJK2NEOXdGd0JvckI4bHJoa0ErN0dqZGxteTNaSXpqT2N0T1FzbTBiRUNRRkcyZkhrTzJuSVVyb3NRQnExaVllY1ozOHY0QzA5YWF6ejU0bDQxUk1IUVMwdytDTHREQmJFZ0ZWeDdMdHRXdlh3cmYyRi9Qd2RyQVRHWVJJK2Y0Tm5WREkycnNYaFMwWFV0SG1PQlEydkpCWTNrUjluVzV5RDZYS1UwUXBMcXBrSlY1dkl3S0Q5VWtqbUlHMzU5ODhUSVlQQU04NElzdFQ3cldsY1A2aDZQOHl5RUdGU2hlRktUdm9ya2lXQ3VoK1ovQmowc2dtdEdLbm15d3VNUVEwNXNWWWVta3R3OThhU1dnbktEeWtOdDFXUTMxWldzRlpwTkowNk9Ca2RaMHRtS0FuUXRrVmJKbUxvVlh3UFRVcDEvdUxBeXdVdk1BemFoRytNUE5XVThrYVZ2SURieHBhSDhoR0tvZWVsc09Pb2ptWGdPWGJib1BXenVFWTJNWGJ0NFVpTm1oWmo3cFBsRTA0bHlacVM1Nkw2YTBZMThZMXlKcjZsajZFOUNNOGw4YjQ0NzY2UFRtaHJQVVhYTVBpQ0VOaVZkUVlKZWJ6U0daQU5KQXNrcTlwakRQUTVYZnFtS01RVEpwNUVvV0x2ZUk3ZnZYWXhkdTdWOFovSEt5NHMzWStkZlhycTNmT25sVTZGVERKUW1FZk45R084ZXJoZEs0cWtSVjdTOXhudG1hOFRGQmpVZGp3RksxUUcya2FJYmgxWXB3TStwd2dnN3BsTzBWKzg4ZGJIbDdHaWRlYVExMm96ZXNKc3hxaEtOcW5GRHo1OVlvK3Jxd3VEK1F4UGVTREtKQnhTQ1p4MXI1aldXeTRzdEtrbW9NWE1qaThSV3Rvc2VOcXFMQVVjRVg5SkcvUHdkQm5BZmY1bjdCeHlVbDlsYU9JQlZlMzFRTHY4cmlXZEtEUTRYQWhudWJwdXROKy9NYlJ1OGEyU0xFMndUQjQ4eUk5QXVpUVg2WjdHV29wSS8vcncybjJWemJkQ3M0UmRMQjhxVlc4N0Y0NnF1TzZvbTB5L2k2KysvcWxBbEt4czU5TldYVjlRVk1DeXlpZ3dqVXpP'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
