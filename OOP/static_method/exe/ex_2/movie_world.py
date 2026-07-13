class MovieWorld:
    def __init__(self,name):
        self.name = name
        self.customers = []
        self.dvds = []
    @staticmethod
    def dvd_capacity():
        return 15
    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self,customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self,dvd):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self,customer_id,dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self,customer_id,dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customer_lines = [customer.__repr__() for customer in self.customers]
        dvd_lines = [dvd.__repr__() for dvd in self.dvds]
        all_lines = customer_lines + dvd_lines
        return "\n".join(all_lines)