def rawr(crop,lon,lat,dist):
  pass

def get_nearby_sales_info(crop,lon,lat,dist):
  return [get_sale_info(sale) for sale in get_nearby_sales(crop,lon,lat,dist)]

def get_nearby_sales(crop,lon,lat,dist):
  return ("SELECT\n\
  SaleID\n\
  FROM Sales\n\
  WHERE (\n\
  Crop = '%s'\n\
  AND\n\
  ABS( SQUARE(Sales.lat*69-%f) + SQUARE(Sales.long * 69 - %f) < SQUARE(%d) )\n\
  );" % (crop,lon,lat,dist))

def get_sale_info(saleID):
  return "SELECT\n\
  Farmers.Picture as pic,\n\
  Farmers.Name as name,\n\
  Sales.Crop as crop,\n\
  Sales.Lat as lat,\n\
  Sales.Long as long,\n\
  Sales.StartTime as t_start,\n\
  Sales.EndTime as t_end\n\
  FROM Sales\n\
  LEFT JOIN Farmers\n\
  ON Sales.FarmerID = Farmers.FarmerID\n\
  WHERE Sales.FarmerID = "+saleID+";"