# coding: utf-8
# вместо suds устанавливать suds_jurko (первый заброшен)
from suds.client import Client
from exceptions import RsAuthorizationError
from helpers import expect_zero_status, expect_int_error_code


class RSWaybill:
    def __init__(self, user, password):
        self.client = Client("http://services.rs.ge/WayBillService/WayBillService.asmx?WSDL")
        self.user = user
        self.password = password
        self.service_user = ""
        self.service_password = ""

    def authorize_service_user(self, service_user, service_password):
        response = self.check_service_user(service_user, service_password)
        if response.chek_service_userResult:
            self.service_user = service_user
            self.service_password = service_password
        else:
            raise RsAuthorizationError("Invalid service user or password")

    @expect_zero_status
    def check_service_user(self, service_user, service_password):
        return self.client.service.chek_service_user(service_user, service_password)  # именно "chek" :)

    @expect_zero_status
    def get_ip(self):
        return self.client.service.what_is_my_ip()

    @expect_zero_status
    def get_service_users(self):
        return self.client.service.get_service_users(self.user, self.password)

    @expect_zero_status
    def get_error_codes(self):
        return self.client.service.get_error_codes(self.service_user, self.service_password)

    @expect_zero_status
    def get_akciz_codes(self):
        return self.client.service.get_akciz_codes(self.service_user, self.service_password)

    @expect_zero_status
    def get_waybill_types(self):
        return self.client.service.get_waybill_types(self.service_user, self.service_password)

    @expect_zero_status
    def get_trans_types(self):
        return self.client.service.get_trans_types(self.service_user, self.service_password)

    @expect_zero_status
    def get_waybill_units(self):
        return self.client.service.get_waybill_units(self.service_user, self.service_password)

    @expect_zero_status
    def get_company_name(self, TIN):
        return self.client.service.get_name_from_tin(self.user, self.password, TIN)

    @expect_zero_status
    def get_company_is_payer(self, TIN):
        return self.client.service.is_vat_payer_tin(self.user, self.password, TIN)

    @expect_zero_status
    def save_waybill(self, waybill_xml):
        return self.client.service.save_waybill(self.service_user, self.service_password, waybill_xml)

    @expect_zero_status
    def get_waybill(self, waybill_id):
        return self.client.service.get_waybill(self.service_user, self.service_password, waybill_id)        

    @expect_int_error_code(1)
    def send_waybill(self, waybill_id):
        """
        Активирует накладную

        :param waybill_id: waybill ID (not WAYBILL_NUMBER)
        :return int: 1: OK, -1: fail, -101: can't delete, -100: auth error
        """
        return self.client.service.send_waybill(self.service_user, self.service_password, waybill_id)

    @expect_int_error_code(1)
    def delele_waybill(self, waybill_id):
        """
        Удаляет накладную (ничего не удаляется, возвращает 0 - хз как это трактовать)

        :param waybill_id: waybill ID (not WAYBILL_NUMBER)
        :return int: 1: OK, -1: fail, -101: can't delete, -100: auth error
        """
        return self.client.service.del_waybill(self.service_user, self.service_password, waybill_id)

    @expect_int_error_code(1)
    def close_waybill(self, waybill_id):
        """
        Устанавливает накладной статус "завершён"

        :param waybill_id: waybill ID (not WAYBILL_NUMBER)
        :return int: 1: OK, -1: fail, -101: can't delete, -100: auth error
        """
        return self.client.service.close_waybill(self.service_user, self.service_password, waybill_id)

    @expect_int_error_code(1)
    def ref_waybill(self, waybill_id):
        """
        Закрывает (?) накладную - вешается красный флажок

        :param waybill_id: waybill ID (not WAYBILL_NUMBER)
        :return int: 1: OK, -1: fail, -101: can't delete, -100: auth error
        """
        return self.client.service.ref_waybill(self.service_user, self.service_password, waybill_id)
