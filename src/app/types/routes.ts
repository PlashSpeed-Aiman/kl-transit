// Types for our data
export interface Stop {
  stop_id: string
  stop_code: string
  stop_name: string
  street_name: string
  latitude: number
  longitude: number
}

export interface Service {
  service_id: number
  route_number: string
  stop_id: string
  direction: number
  zone: number
  sequence: number
}

export interface Route {
  route_id: number
  route_number: string
  route_name: string
  route_type: string
}

export interface RouteStop {
  route_number: string
  stop_id: string
  stop_code: string
  direction: number
  zone: number
  sequence: number
}

export type RouteStopWithData = RouteStop & {
  stop: Stop | undefined
}

export type DirectionMap = Record<string, RouteStopWithData[]>
