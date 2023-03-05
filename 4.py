# -*- coding:utf-8 -*-
"""
@Author: Rainbowhhy
@Date: 2020-11-14 15:16:18
"""

import os, re

def is_public_ip(ip):
  # 判断ip是公网还是私网
  private = re.findall(
    r'^((192\.168)|(198\.18)|(198\.19)|(10\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d))|(172\.(1[6-9]|2[0-9]|3[0-1])))\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$',
    ip)
  if private:
    return 0
  else:
    return 1

def convert_unit(unit):
  # 统一转换成bit后计算
  if "Gb" in unit:
    flow = float(unit.strip("Gb")) * 1024 * 1024 * 1024
  elif "Mb" in unit:
    flow = float(unit.strip("Mb")) * 1024 * 1024
  elif "Kb" in unit:
    flow = float(unit.strip("Kb")) * 1024
  else:
    flow = float(unit.strip("b"))
  return flow

def get_traffic():
  # 调用iftop命名获取公网和私网流量
  iftop_info = os.popen("iftop -t -N -n -s 4 2>/dev/null | grep -A 1 -E '^  [0-9]'").read()
  iftop_list = iftop_info.split("\n")
  count = len(iftop_list) - 1
  public_traffic_send = 0
  public_traffic_recv = 0
  private_traffic_send = 0
  private_traffic_recv = 0
  public_ips = []
  private_ips = []
  for i in range(int(count / 2)):
    # 获取出向流量信息
    traffic_send = iftop_list[i * 2]
    traffic_send_lists = traffic_send.split(" ")
    while "" in traffic_send_lists:
      traffic_send_lists.remove("")
    traffic_send = traffic_send_lists[3]
    traffic_send_float = convert_unit(traffic_send)

    # 获取入向流量信息
    traffic_recv = iftop_list[i * 2 + 1]
    traffic_recv_lists = traffic_recv.split(" ")
    while "" in traffic_recv_lists:
      traffic_recv_lists.remove("")
    ip = traffic_recv_lists[0]
    traffic_recv = traffic_recv_lists[2]
    traffic_recv_float = convert_unit(traffic_recv)

    # 计算公网和私网的总流量
    if is_public_ip(ip):
      public_ips.append(ip)
      public_traffic_send += traffic_send_float
      public_traffic_recv += traffic_recv_float

    else:
      private_ips.append(ip)
      private_traffic_send += traffic_send_float
      private_traffic_recv += traffic_recv_float
  return public_traffic_send, public_traffic_recv, private_traffic_send, private_traffic_recv

if __name__ == '__main__':
  public_traffic_send, public_traffic_recv, private_traffic_send, private_traffic_recv = get_traffic()
  print("公网入向：%s" % public_traffic_recv)
  print("公网出向：%s" % public_traffic_send)
  print("私网入向：%s" % private_traffic_recv)
  print("私网出向：%s" % private_traffic_send)