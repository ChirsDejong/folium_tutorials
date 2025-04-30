import folium
from branca.element import Figure

# 上海坐标
shanghai = [9.35, 116.10]

# 创建地图
m = folium.Map(
    location=shanghai,
    zoom_start=10,
    tiles=None,  # 不使用默认底图
)

# 添加高德地图底图
folium.TileLayer(
    tiles='http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
    attr='&copy; <a href="https://map.amap.com">高德地图</a>',
    name='高德地图',
    max_zoom=18,
    subdomains='1234',
    overlay=False,
    control=True
).add_to(m)

# 保存为HTML文件
m.save('gaode_map.html')

# 打印提示信息
print("地图已保存为gaode_map.html，请在浏览器中打开查看")