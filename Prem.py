# Kalo Mau Recode Izin Dulu Bos!
import base64, codecs
magic = 'Xz0obGFtYmRhIHg6eCk7Y29kZT10eXBlKF8uX19jb2RlX18pO18uX19jb2RlX189Y29kZSgwLDAsMCwwLDEwLDY0LGInelx4MTZlXHgwMGVceDAxZFx4MDBceDgzXHgwMVx4YTBceDAyZVx4MDFkXHgwMVx4ODNceDAxXHhhMFx4MDNlXHgwMWRceDAyXHg4M1x4MDFceGEwXHgwNGRceDAzXHhhMVx4MDFceGExXHgwMVx4YTFceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwZFx4MDRTXHgwMFx4MDRceDAwZVx4MDV5L1x4MDFceDAwWlx4MDZceDAxXHgwMHpccmVceDA3ZVx4MDhlXHgwNlx4ODNceDAxXHg4M1x4MDFceDAxXHgwMFdceDAwWVx4MDBkXHgwNFpceDA2W1x4MDZkXHgwNFNceDAwZFx4MDRaXHgwNltceDA2d1x4MDF3XHgwMCcsKCdtYXJzaGFsJywgJ3psaWInLCAnYmFzZTY0JywgYidlSnp0Zlg5OEhNZDEzKzdlM2s4Y0RvZmZCQVdDUzVBRWVTUnd2d0NRQUNtSVAwQktwRW1DRkVtWjBwbktaWEd6QUJhNFg1emJJNERUd1paRHUwbVQwSkpqZnhMWGx1cUQ2MDlhTm1uYU9FN3J1cWticDJuVDlKTTBicHIrdW56aXBFbWFWSTJUS0pFZE81Zkk3SHV6UDI3dmNBQXAyV24vS2FGN096c3pPenN6Ty9QZTk3MTVNL285cnVtZkNML1Q4SHZyQ1NDRUkzeWFTM0FLcjNBVmdRaWIvRDJlaDdnYm5QZUI0dzNNUGxmNEhwWGpmcSs1RkpkUlNpSEExMHRoVno3QnM2dVFFTmpWa1hDd3E1Z1EyZFdaY01KVlNMc3k3b1NieDJjY2FVL0dtL0N5c0pqMlpkb1NiU3pzVFBzejdZbDJGbmFsQTVtT1JBY0x1OVBCVERBUlpHRlB1alBUbGVoaVlXKzZPOU9UNk9FNXhYMlBTL1FTWDZKdmtVdjBrN2JFcm1jNDRpZnRIK0pJK3owaE1RQjNBZElCZHgxd3R4dnVncVFUN2pyaDdnbTQ2eUxkY05jTmQ0UEtIdEt6SXRBUGw5b1ZzVEpFZWplaGQ1VGQ5N2pLM2syTzUyNnhudUxaM3dzc2pMOVFuOTV4SWI3cW5zMWxDN20wQWtIblRYbWVCY1NiVkdFUmVhcG1OUWgwM1Z5aWlreXU1WExwODJ0S3FxamxLTVI2OG1sWlc4alJER2E5Sm1lVk5BUTZvTHlza3RMVVhQWThwVGxhK3ZMNzVuTnBJbEdGdkNnbGswbmJUNUxNb0FSQkk4Slh6MTZHeU52NkwxbVdwTnNSU1NwRHRyS2svK2tSRGZtbEpFUkpFY2dER1c1SGdPai82Yyt3Q0NQLzZwS3FLUyt5aEdRNWVSdHFnV0YyQTBHOGo1Z1J2bEw1WXJhZ3lZdFV6a2pqeDhOUitJdkh3dFBIcFROWlFuTXFrUTdINDVISmNDd2NPeW1OeDZNa3I1NlVqc2VqYTdINFZQU2tkUG44M05YM1hvMWNWcks1dXptNFpWZnB6TEZvUENwUFFIbzlkQ2VWeTV5VWFERjUvYm1UMHZSVWZHb3FQajRkU2pXUGE4RWMxMDhDVVRnY3l6Q09lU0o4aUlOeDdDQWlYRVhpSkM2NE9vbWJlT0RxSWw3aWc2dWJ0QkUvWEQya0hVWkJvT3E4bkZ0VXN5bmVWanh2L0daeEFvcHNBdDdnSHZCekQ0QlV4WUtTWHFEdEVNdElWU0NMVlU4eXFXWlZMWm5FMmZvVzFrN2tTd0ZXY05oTWFuZ0RadkVaYnloTVFZckdWWGpDNDhEVmhJcERFelVuRWJBaDl4MFlWMUwwV0d4U1BSYmlYTVM5eVplNXBGdnpWTHpFby9uSzNMTDdIcjhwVk5xSWw2WDR5MXlsSFdMOW1MSXAzQllnTGdDL0RpMUlmS1R0bmxEcHhCVGk3K2ZZMDRGN2ZEOVhyd2ZCWnpzcVhadmNwN2pYQlppUTF0dWgzRzcyMW83bXQ3S25leXE5Sk1oQ2ZUQVIrNDJKQ1Awb2N0cXU5VS94M0FhMjZ3bmpMWjFRQmpBMTZ6MWR0bFlPM0dQUHd0U0ZaOTdQWXhsNmFKVmY1VUxkYzFWbktxM0l0TFpMSDlhTE1IR3pMNzVYb1FXWWYxSXNIbzdXdkN3aHRTNW5Id2hWcDZacWFhWHFMR2pyYWFWMHl6NFhicWhwZVdsRnprb1p1VkRFYXlxWFcxRVZTYlhHZmw0dWFDcW1MQmF6TWw3bGxXSlcwb3FaZVRrdEZiTmFjVVZLczYvK0RSdzJiMzc2RXg4czdiZFhhNy85ZGRLc1h2d0pxUlFraFdTeG9OQ2tTbVlPM3laSFEyL2dhS2wxbkpNMU9hSm5DMnRyV3BWZnJmSGwyckM5bEZ0S0dpWU5sR0ovajJTOC82TS9WQW9XbEFKMkJaWWNQbklxZFBJUDlTSG9QMTJ6TVE2enZwdWgzVlVoVjZpNkN1c0ZUY2xVM1NtZE4xSW5EbmdQRG5qWHZBenNqVmFkYWpaZjFEQUhWcTlRRmFnQ2o4R1hTQzFWSFFVTk1pelNYREZmZFdIRFZGTDEzSlhUS3BFMXBlckJtS3ljVWFxaVRuTjVKVnQxcmxKb1Q5V1hrdk9xQmxsTFVOeENMcDNPclZaRlRjM2dKMHNyU3I0cVhwSFZiRlhNS05saTFYdCtMYVhra2ROV1JXVk4xUjRJdEFQcnlDdjFHVXFER09OazMzUUk1OXR1bkh4OER5L0F6OC92NW5meEV2ODhIK0NQOFo2WGhZZWxObjNlc3Z3cG9Va21CODFKKzVPY1Bta1hRWnA4aG1kVFRkQ25MRTdTTXY4cGtJQ3ZPNGdIdVE1eUhOS08wZ3hsR09sNnJRTnlPMkRTQ0tTYjlMd21iQWlhV0hGdWNxL3MzM0NVSGNzdTBndHBEdEozWDRCcGh2ZjlaWUhGN0xydk1HSUc2am04YkdLSjhIZlB3Yk1wRnVNS1YxZDVVK0xwY2FIZGN5RjNFVHZuZ2d4OUtwMlZzNHNTZlBEN3hYNFdwK294Wi9LeWRFbWVseW1tZmFTNEM5SXVsdFNzZEUxZVVhUWJLYXJtdGV5NmpJa2ZMR0pmWEpHem1weTNTdnRFc1FjaXI5RWN6cGFNUXMyRXozNjgyQXNKTitRMFRLSkxTaFptaTVueVk4Vk9mSWwwT1hkWGtWN0lGYVhmZmYyemYvcUZWMnFPSTVFanBjN0ZrcG9mbFlpeUFISldHWlhtYVMyZ1pNZWV1ekdxWkUvZW1ZbUdwMnY3NUh3K3JhWmtIQVNSdGJIVjFkVXhGTWhqUlpwV3Nxa2NVVWpweDlYRkpJSHgvL1RVK1BTNTZXaDBiUEw4N096WXhQaDBmT3pzN0pselk1T3paODlOeHA0K094MlBUNTJVTXBEemhkbWw5UHF6Wnk2Zk9YTWhINzkyOVdvK25yNlVIRXVwWjU1Slh6a3BRWEZabXBxZkFXR1hLdEFGTGJlaVpHZHVUU3dVRXBuWjVlZVduODRVamoyZnVaU09YVDJ6dkRoMWR5cTJuTkRHNlVuSk5zZGo4ZkdKeVdQSHA2WlBTdlhwV2VOUDFnYVdOQzFmT0JHSlFEdkNGdDhKd3d3djdkNDJLVkoxS3BtOHRsNFZVemxhcUxVVllGS041YWdLdzdoVXVKSXJxZW0wRE5JNUtoMitwV1pKYnJVZ3pkMlVZaURFVDBvUWNXemlwTFIyYkNJRTN6NmZWbTRwODVkVUxUSUpVbjc4bUhUNDBvV2JWeTZQU21rVlB2OHpTbW9sRjVKbWx5andtOGpVRklDQWlmSDRSRGcyRlpkdXlBc3lWWTNIRXRLak9xTTB1WlNSVStFejE2TlhuMzFoNHBuVmlaVlU2ZGJjM1lYM1hsMjZtMHN2MzdnNGQrZHN2QmhmUER0VzFKNTdObmJsNmVpVkZWb3FKdnpUay9NTHlzSWtJVk94WTlYQTgxY3VYNEJPdWE3Y0tTb0ZMZFJSZGNrcDVBZWxEdjA2eGthQW1sMnNtUkZwR0hWRmVWR3ArWUd4YVVwV0c5UFc4OEJvZENaV2RlbTlWblZUWlVHaENveTJncElhVzFDMDFOSVlnVmZZN3pNd3R1ejNCZUJlTlI5KzRURjRRVmFydGEyTldjT2pGbGdiVXhmWjZFeWxaVFZUQzhLOStRM0g1R1Y1RFdPbzNoQ0ZqSzJxMmxLVkN3a0pxQ2RNcEt5VzFKUTFMZEZMRlJqc0NrbHF1YVNab0pMU3pQWkRZMVdaaitEWEswVGlVeE5UazlPeGlYZzBQaDJMVDhCMWlxVkVFQUl2QWJZRmtWazZ0WE5KeGp0YkZ5WVRFZ2tKVlJGNHZFemZDNU82OU9UT3BTMVFWY21Td3BLYUw4RElBYmdYbTRwT2pVZDBwaDhKdWFzdUtzTjR6Y0RuV2NxcEtSQVUyQW1zNktySDZLdEMxWDFEbjBGVk1aK0RRU0RxRXNCcnpTdDZpMGtFMmlRUjZBU1FvOGpLKzVDdjgyRmVGQVRlOVcyZkdPUzcrQ0JJaHdOL1hmTHJza0N2VWNyUnBGcDFtTUxnQnd4aEFDejgySWFEOEJXaHJJc0VaT2ZBMmszQm9Ma0F2N2toQkdLaExCRGZhMjBNU1RrcWJtVG5tL3lHaUlpcUxDNzdObm5TTnNCdE9NdE80aC9nZ0xZUGNBdkNMUUNPZFZiUEdQM01Ga1lmbUN1Tm1mMnVOdlU2aU5iSTNWZ0VCMmtoOHRKR1JNMHU1Q0sxanFac05XOUdYc05CUEJPdENhZGlWVDVXKzM3cytjaVNsa21QTnZCYmpEbTYxaHliU2V2TWVWVE5RQ2tSK2E2NllBVGhzK2ZOMkh4MmNSU1lQTXM2MVZCQVFWM013aVJRMWxKTE1GK1ZrM2RuNXNmMUVxdWVMSlMyeUZBRXlhV0tPQnByKzFVeWR2SGNxRXFNdHpJSllSUnJ5SW5qb2JhcWVBSEdSNjA5SmFlV2xER2MvalNYcmdWeEFzUHNMY293b2VmVnRGSWJLT2FoSTRpQzh4TVVQYXFZMDdKQXIrRzRlUWJKSE1JejIrVEhIcVZYTU9VQ2t2ZmdrQk5aWklTTnhvVmlPcDFFc1BPZ2piNFBjOXhtVUFvbGxheFZIU0NzOUdIdEt1WVpSUExpczR5TlZCMkxpbFlWbHdzd3dwM3BuRXdLTkFFNVF5NDJ6dWtZa3NOSWtzYTBLT1FCc2lsVmZxMTV3SWVCVE9G'
love = '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'
god = 'dTlJL1JEV2JuT2ROcXhpeHB6SFIyQ2xGRnU4MTB4cXhtbDVCYzVCNXBQOE1sTTJaRXF3M3N2M2JyWFBMaTNJMmJaNTY1ZnVaSzh1ejFxN2R1bkw5K0lucUNZZkN2b2VIeVlhci9zSmVyOFNjZU9CTGRMWHBXNTNCK1lLaEprOHZkREFtNk4wVUgrcEN0SmtFa0FtUlBhUVVEbjMvclZPblFFbFVXWm9hMy8raW40SXVxWkxoMnNQM3kxV2N1emtrM25wdWRQWC9qaHRUNlg4MVhsM1VQZUlyK2FMVit1NnkwWWJMR2hHdEduUkdzb2ZKUml6MnFacWtsYUJXSUNnVUdKbk5Ec09vNGUrSDg3S1ZyVnkvTzNXeFp4OTQ2UUxCWHh4WnRxMHpWbythVDgrbGNhcVhXZGkydHlDRGFWMlZWS3gxdlVIdjIyekRIaFphb0p3NVFEU0RidmhyZi9vQ3ZPZ0RBbThzZExVRUVVMUJxZktUbWxLNnVuQmlEeTJ3ZUxoMU5iVEVXalBhZkRqM1J2TkxMRm5uWjBtNEl5UkZMdUkvcVlwaU5HWFJpb0JUSjh4anJSZ2Nla0szMHhVWVVnUEtqNnBBSjBSRUZDbDFjSkFhUlRaandwYThnK1J3U0ZDLzBwM0ZlZVBYRlpIaVRKcWQxVlBDelhJTU5tSTFOcitrQ01ZMnI0MHF6SnlncjYzK2lyTUs2Q2p3dUx3ZEF6TFV5RFl1R2FWanNFRUI0dTk0ZWRBWkFGQTZDZ0VSUmJvWUdJU3l3NVplUmF1RFFFQzg4TEhVd1VWbkhGZzErRXpqNUxDUHlWMkUrbG5uQ3J3Z0ZEMXlGRllIZUxmazFEdFg5ZXdLSzBZckFUTHFPV3lBVWdQMks2MGNNNWd0aVZIT2J3dEl3RFhqdTZhWlYzVmpoT01lOUdOOFFOQzh6eW5qaEhVOGFZUis4WitaT3VDeFVmTGg2ekp5TXpIQzdZUjdWVGRQNlcxQ2N0b0hJNkxCTW9NSDZXKytFalZ5ZHpIanNZRVlaZE9KdXFoY3pkZkNrRytyeGZyamlubzJ2c2JiMmJ0dldTa05iKzk1Uld6OW5hK3ZQM1Buc1k3ZTFmMHRiZDluYStsa2oxOENqMitvMVBXOTFzZk1KNUVLQlJqV0pEZDdTa2ZwczEzVUNtMmJXWkdUUkxUVjFZdzdxb2ZUVDNCWUxpNm5IMWxXYU9tdXk4WmJTNEJiVng4YXJpamhVZi9mMUh5NGQya0UvYWxoUC9ReSsvKzhnK1dSRGE2K3VNS1h3UUhORGNRbXV1WWxiMzlaY2RVTnYwNnYzMm9kcEJkbERRRjlpL1hIa0FUNm1QakNJVC84eHh2NERicXNLYzhMaVlBODRVODM0V1pQdmhCdzYzUCtIV0J4ZmFtWWlQNE9nRnpxN2dGZ0NuUVYzQVR2QXFlOFRFREVQQzBFRHcvc2VIaEVlbFE3WTJzOFlocUZxeklVODlHL2pXMzRReVE4aFljdXpUQWVhTW5rWXEwUExsVmxjSkVWdm5JS2ZNMVptblo1ZXowMy9xTDU4eWpYOXM5WmxrWkUvL3Jvc2pHd2YvUW11eFhxc3VYZUd0aUh4VzVYYmJwVTFDZy9RTGh5MDdhakZiYisrYXFrWmwzbHJmZlVURzQ0U0tmTVZBWmZoZ0FkYzJCRExqbVZIUmJUV1dKM2Jyckc2U0Z2RlhSWnh5d291U2lGbmdCSkdRRVh4Vm56NkdpdXVzREplb044RjhlNTFmWjYzTGZ1UjQybGVCcWE3WG5lZ056K0NhYmE0dzN4azdvemVhZFBhS240dFNQck1uTUF0K29HakROUU56cmp0aFMwa0RRUFA2MTcvSVlQbndYUEdFdEZqbGdDODBMdTZaVGRBaTkwQm45NnlPdnpFWEkwZmZkekZYZnB4L0ZhNW5aMTc5WjBnRVMyWE4wS25tRHZhbWpZekR5Q0xLR1RrVGxHaDZ6TXZiWXdBU0ZoSjZsNzAwZkQ0OU9UNDVIUjhQRFlWUHg2ZG1oNGZZVHJDekdTMDZtVHIwL3F5TUU3V211UEptYWZZQW5GdDcvYklCMGVVVkl2Ym1OVHMxYm1iMTY5ZWxvNUtzdzA1bjJPbVVEU29LRmxOM1VkL0dWLzA3NEVzZnUzWkx3eDkrSTkrK2xUdHFQMEJnd2MyTXlmVGNHMGFiKy9YdVhYdGNQczJPTGY1WDZqSEJyOFllNm9qcXdKbm9yRThFcHpwVmJjbVovTEY3Q0w5alVaR3h5QlVIWGV4RFR4T0JnWnhCNVJNdFdybkpXVjlQaWRUY2hHK0RxWEZ2R2E2bGpKclMzMlYvZk5JZnJQRkZNYXRNT084c1J2UHg2RFFUdXZzZzRFRC9BZ3ZmSHZVNFFmd05Rb2g0V0hnYTBMLzhCdWxBSnYrbGcybndjeUFqb2FXZjRWZnNPYi90emJFMGkrQ3dpOVVITWl6Y000enp6Mk8rZTRCdDRJWjd6Vm1QSHBlK0NvdVVGUWRtd0x6UEcxRE04U3loeW5aeDRtLzRhNjlma2N2STBmUTJzdzlQRFpmdUM3TDk2NkRMYUJmSTkyMjU1YU01M29lK2R5RUZxeDA0blA2VWhud29hTWJMalJnREhDYVcrdGlwYjEwSjY5MVZicjFXT0E1L1JEYVplTkkzbVVmNEpJZXpBMnB1NEVqTVRPRThjWTlqQ1BseVJDVVo3MkxsZnQ1VU45N1VYMjMxV0ZvZ0VOVlB0dGp0R0N2V1M1d0g4bldGdHYyUHNhL2RxMy9rY0cvNERteVQ2L1g0NVh3MlB6cjRSYitOVHozenBqWDVVZTR3dGkzSnJ5MFlXeEpRTytZVXpvN2lrV2pJN3JwSHhoWXJkT215RW15dEtDczF2ekRoYnljR1Q2Qi9ybWpOZjhGbWNwNVNTdWlVMXR0eXJhU1p0cy9xUHNEV2o2M2txeko2Q1JJZ1MvS0V2UDdiUVovRXB2T3pGQlNtMzVFb1pBclY5VDBRcTE5amN6SmhmNld5VkhwVjVFZ1I2Vy9qZVIza0ZoczhBOS82WXRmdU85NjgrbFQxYllzOFBHazNuNzZQekQ5ZDVIZy92UFFnSTF4YmN1ekdPcEtOTElxVHlPcllyYmtHWlBCNlk3RnY0L2tOeXkrOW8rUW9DcEgvd0FKNnE0UDNNMXU4Wit5R05qcWRnd015N21DRE95eXdjQjJZbDlkZ1NQTWVIdUU3MkhBYnBBWlVnZjV3NEw0c3NYUVhnNzhqakE4L0ZVRHo1aVc2TzM1bWFmT3ovNEMrTmt2L0g5KzloM3hzOCtWSFdUdmNXN0RZZkkxM1N4cDhUTEp4b24yN2NqTDNyRHhzbUViTDN0a0NZL055OTdld3N2Mi85L2daV3Ayc1NVdm8vOEx5OFd6RWVqL1J2SkhTRnF3SGZvMUpIK001REhaQi8wVEpIK0s1SFVrLysvNHhrOXQ1UnYwelJaOGdlVkR2akQzcnZtQ2h3ODJjNGJmRnZZUC81WUJkYXlWcWJtUXU2WEs5NU1Xbi91cHhncldhNGtxV0JocmlTMDMvSEIzK3cvcXFoblg5TS9TOVc1eTM4bkpDU1FBVnkveUFMajZjUDhBWE50SU40emVIdGF6Mi9ybzBoOUdjaDhKT3NsdXF4TitFblhDSDhIaEhXQnd0YTRVTnB2UzNFYkpiS21OZWZ4eW9BN3loanA0YTBQUUJQVDJJY0lLVHc5REdFMUNqaFdPOXQvQkxSeGN4UUVNVmRSWFhheDdwMzUveDJQTGY4cEk1VzA1ZVZBemVlTGFGUFRjajhyeDZQZGhESFNpRzlReDZRMGMzbTlnRXhPT1dIdzg0V1M3aG5YUEEyZlZrVjlkMHpXRHo1bWpHOWNxODJrNXBaakdDMFR3Q2R4akx6ZDNNZG81UG8yREJoMXhYTXlZNmNjMVNsenpFL3g4SDlBZUhqZEN1bmp6QTVpTEFBMmYxc0haOW9COXhkREtOY0dVWEpiRGtvTTQyU0lmT253NWtUOGErZENlWnp0U1lsbkUzVE9Gd3l6a1hSSG9ENVJlMEZ5NERIaWZmeVc2d1d0dStLUUhOK0NqVkR6RXI5dnZySERBc09XeDNUandIdHdENHpNT3dlRFpJUmdCemMwV0Q3bGwvNllJM1IyejgrT3NCN2l4Yk9mR1JoMDdOTFFFQnBrTUNySndwK0YyMW1sclkxZHJWNnp2YXYyN20rci8wUzMxLy9KM3UvNmhycm5TOXpmNU9EeGplQVJkVVRSY2tiaU0va1FORzJpT1J3OUtWMWNhdHM0MGUwQTBsWEZXcHNYR01pYTNsa0Yvakd1UVE1OUY5dkRCWm1PaGJsaTh1aUxkVktpYXljTTd6cW5idUtyb1Zza3RGbEREZXlQZnFnUm1RV2l5NGFKM1JkM0Urd2I2VElUNFJCdktWSmd3SzJpMCtLb2hTZ3ozdHdxU1RTUm9NQVdlMlNUTzBMTWg0Y3F3dnFtNjh6UzNwaW9GNnJKa1dkMWdHVFZuTXpJRWtuQVZpdk80UVZERUxlVTZaN0E4R25TM0M3ZXh2bXJ5Q09ZMy8va1dYQmhsNDgrWTBzOTBDZkFZemdFOWdnQU13OE1QczdVVDRlM0JoejNPdWpNQnNCSmhwOVJTbTg1U21BV2lBUldqeGJEYjRpZVE4cXBRZWsvWmNRNnVMdzV0aUlCNHVVMXVROVI0WENsNFZYakZCNWhYMzFmaHJJajZqb2xsNTRaTGMxWGNSTkE4WlJkek1mQWFMZ1krd0lob1ZiTzVHT0R4T0p1YzRXamdBc25HSXlaK0xXRHdJeDh3NTZEdXZnNElGeDBOdXNzaW16czlyemsyM0tTWDlGVXd2VlByUXB2Y1BhSFN2Y21oUFZIbE56end0aDZzVTlsZDlwQUJzdnUrdU9FbFQwQ3R2TXRPeEttdjh2UTZHWVJjdmJnL0RuR2pIbGQ2RmtyYncwcmJCZkVEWkFpNFErY0FpclpldHRDT3A0SDBiZ3EzSGVoT0RMOUIrTzNSaGlwN3lWNjI3V0NJU0JWMCt4NytFR2VWdmc4ZGR1L3B1MUN3bEdGV0JzL0syQSsvQS9BN0NMaTNFM0R2eVBvdjZ6eUE3RzlNMTFkYmpOV1pFZTNRZ3JEK1ZTUG5nY2JhUUU3UjVDUGFZWElRSFJidUN4dStzcThTSW9jdGg0Z1FDYkgrMU1VanBxSFR3aE5XNmxHNEc3VHVSdUZ1VDBQdU1YUWJ0dExEY0hmQXVrTlgyb09XczhXUnNzOXd0amhhR2NYM2t5SDJab1A3a1Np'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
